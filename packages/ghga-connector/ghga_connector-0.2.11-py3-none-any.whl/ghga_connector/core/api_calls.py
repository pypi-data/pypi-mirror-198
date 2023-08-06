# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Contains calls to the GHGA storage API
"""

import base64
import json
from enum import Enum
from pathlib import Path
from time import sleep
from typing import Dict, Iterator, Tuple, Union

import crypt4gh.keys
import requests
from requests.structures import CaseInsensitiveDict

from ghga_connector.core import exceptions
from ghga_connector.core.constants import MAX_PART_NUMBER, TIMEOUT
from ghga_connector.core.http_translation import ResponseExceptionTranslator
from ghga_connector.core.message_display import AbstractMessageDisplay
from ghga_connector.core.session import RequestsSession

# Constants for clarity of return values
NO_DOWNLOAD_URL = None
NO_FILE_SIZE = None
NO_RETRY_TIME = None


class UploadStatus(str, Enum):
    """
    Enum for the possible statuses of an upload attempt.
    """

    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    REJECTED = "rejected"
    UPLOADED = "uploaded"


def initiate_multipart_upload(
    *,
    api_url: str,
    file_id: str,
    pubkey_path: Path,
) -> Tuple[str, int]:
    """
    Perform a RESTful API call to initiate a multipart upload
    Returns an upload id and a part size
    """

    # build url and headers
    url = f"{api_url}/uploads"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    public_key = base64.b64encode(crypt4gh.keys.get_public_key(pubkey_path)).decode()

    post_data = {"file_id": file_id, "submitter_public_key": public_key}
    serialized_data = json.dumps(post_data)

    # Make function call to get upload url
    try:
        response = RequestsSession.post(
            url=url, headers=headers, data=serialized_data, timeout=TIMEOUT
        )
    except requests.exceptions.RequestException as request_error:
        exceptions.raise_if_max_retries(request_error=request_error, url=url)
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code
    if status_code != 200:
        spec = {
            400: {
                "existingActiveUpload": lambda: exceptions.NoUploadPossibleError(
                    file_id=file_id
                ),
                "fileNotRegistered": lambda: exceptions.FileNotRegisteredError(
                    file_id=file_id
                ),
            },
            403: {
                "noFileAccess": lambda: exceptions.UserHasNoFileAccessError(
                    file_id=file_id
                )
            },
        }
        ResponseExceptionTranslator(spec=spec).handle(response=response)
        raise exceptions.BadResponseCodeError(url=url, response_code=status_code)

    response_body = response.json()

    return response_body["upload_id"], int(response_body["part_size"])


def get_part_upload_url(*, api_url: str, upload_id: str, part_no: int):
    """
    Get a presigned url to upload a specific part
    """

    # build url and headers
    url = f"{api_url}/uploads/{upload_id}/parts/{part_no}/signed_urls"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    # Make function call to get upload url
    try:
        response = RequestsSession.post(url=url, headers=headers, timeout=TIMEOUT)
    except requests.exceptions.RequestException as request_error:
        exceptions.raise_if_max_retries(request_error=request_error, url=url)
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code
    if status_code != 200:
        spec = {
            403: {
                "noFileAccess": lambda: exceptions.UserHasNoUploadAccessError(
                    upload_id=upload_id
                )
            },
            404: {
                "noSuchUpload": lambda: exceptions.UploadNotRegisteredError(
                    upload_id=upload_id
                )
            },
        }
        ResponseExceptionTranslator(spec=spec).handle(response=response)
        raise exceptions.BadResponseCodeError(url=url, response_code=status_code)

    response_body = response.json()
    presigned_url = response_body["url"]

    return presigned_url


def get_part_upload_urls(
    *,
    api_url: str,
    upload_id: str,
    from_part: int = 1,
    get_url_func=get_part_upload_url,
) -> Iterator[str]:
    """
    For a specific mutli-part upload identified by the `upload_id`, it returns an
    iterator to iterate through file parts and obtain the corresponding upload urls.

    By default it start with the first part but you may also start from a specific part
    in the middle of the file using the `from_part` argument. This might be useful to
    resume an interrupted upload process.

    Please note: the upload corresponding to the `upload_id` must have already been
    initiated.

    `get_url_func` only for testing purposes.
    """

    for part_no in range(from_part, MAX_PART_NUMBER + 1):
        yield get_url_func(api_url=api_url, upload_id=upload_id, part_no=part_no)

    raise exceptions.MaxPartNoExceededError()


def patch_multipart_upload(
    *, api_url: str, upload_id: str, upload_status: UploadStatus
) -> None:
    """
    Set the status of a specific upload attempt.
    The API accepts "uploaded" or "accepted",
    if the upload_id is currently set to "pending"
    """

    # build url and headers
    url = f"{api_url}/uploads/{upload_id}"
    headers = {"Accept": "*/*", "Content-Type": "application/json"}
    post_data = {"status": upload_status}
    serialized_data = json.dumps(post_data)

    try:
        response = RequestsSession.patch(
            url=url, headers=headers, data=serialized_data, timeout=TIMEOUT
        )
    except requests.exceptions.RequestException as request_error:
        exceptions.raise_if_max_retries(request_error=request_error, url=url)
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code
    if status_code != 204:
        spec = {
            400: {
                "uploadNotPending": lambda: exceptions.CantChangeUploadStatusError(
                    upload_id=upload_id, upload_status=upload_status
                ),
                "uploadStatusChange": lambda: exceptions.CantChangeUploadStatusError(
                    upload_id=upload_id, upload_status=upload_status
                ),
            },
            403: {
                "noFileAccess": lambda: exceptions.UserHasNoUploadAccessError(
                    upload_id=upload_id
                )
            },
            404: {
                "noSuchUpload": lambda: exceptions.UploadNotRegisteredError(
                    upload_id=upload_id
                )
            },
        }
        ResponseExceptionTranslator(spec=spec).handle(response=response)
        raise exceptions.BadResponseCodeError(url=url, response_code=status_code)


def get_upload_info(
    *,
    api_url: str,
    upload_id: str,
) -> Dict:
    """
    Get details on a specific upload
    """

    # build url and headers
    url = f"{api_url}/uploads/{upload_id}"
    headers = {"Accept": "*/*", "Content-Type": "application/json"}

    try:
        response = RequestsSession.get(url=url, headers=headers, timeout=TIMEOUT)
    except requests.exceptions.RequestException as request_error:
        exceptions.raise_if_max_retries(request_error=request_error, url=url)
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code
    if status_code != 200:
        spec = {
            403: {
                "noFileAccess": lambda: exceptions.UserHasNoUploadAccessError(
                    upload_id=upload_id
                )
            },
            404: {
                "noSuchUpload": lambda: exceptions.UploadNotRegisteredError(
                    upload_id=upload_id
                )
            },
        }
        ResponseExceptionTranslator(spec=spec).handle(response=response)
        raise exceptions.BadResponseCodeError(url=url, response_code=status_code)

    return response.json()


def get_file_metadata(*, api_url: str, file_id: str) -> Dict:
    """
    Get all file metadata
    """

    # build url and headers
    url = f"{api_url}/files/{file_id}"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        response = RequestsSession.get(url=url, headers=headers, timeout=TIMEOUT)
    except requests.exceptions.RequestException as request_error:
        exceptions.raise_if_max_retries(request_error=request_error, url=url)
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code
    if status_code != 200:
        spec = {
            403: {
                "noFileAccess": lambda: exceptions.UserHasNoFileAccessError(
                    file_id=file_id
                )
            },
            404: {
                "fileNotRegistered": lambda: exceptions.FileNotRegisteredError(
                    file_id=file_id
                )
            },
        }
        ResponseExceptionTranslator(spec=spec).handle(response=response)
        raise exceptions.BadResponseCodeError(url=url, response_code=status_code)

    file_metadata = response.json()

    return file_metadata


def get_download_url(
    *,
    api_url: str,
    file_id: str,
) -> Union[Tuple[None, None, int], Tuple[str, int, None]]:
    """
    Perform a RESTful API call to retrieve a presigned download URL.
    Returns:
        A tuple of three elements:
            1. the download url
            2. the file size (in bytes)
            3. the retry-time
        If the download url is not available yet, the first two elements are None and
        the retry-time is set.
        Otherwise, only the last element is None while the others are set.
    """

    # build url and headers
    url = f"{api_url}/objects/{file_id}"

    headers = CaseInsensitiveDict(
        {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )

    # Make function call to get download url
    try:
        response = RequestsSession.get(url=url, headers=headers, timeout=TIMEOUT)
    except requests.exceptions.RequestException as request_error:
        exceptions.raise_if_max_retries(request_error=request_error, url=url)
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code
    if status_code != 200:
        if status_code != 202:
            raise exceptions.BadResponseCodeError(url=url, response_code=status_code)

        headers = response.headers
        if "retry-after" not in headers:
            raise exceptions.RetryTimeExpectedError(url=url)

        return (NO_DOWNLOAD_URL, NO_FILE_SIZE, int(headers["retry-after"]))

    # look for an access method of type s3 in the response:
    response_body = response.json()
    download_url = None
    access_methods = response_body["access_methods"]
    for access_method in access_methods:
        if access_method["type"] == "s3":
            download_url = access_method["access_url"]["url"]
            file_size = response_body["size"]
            break

    if download_url is None:
        raise exceptions.NoS3AccessMethodError(url=url)

    return download_url, file_size, NO_RETRY_TIME


def get_download_urls(
    *,
    api_url: str,
    file_id: str,
) -> Iterator[Union[Tuple[None, None, int], Tuple[str, int, None]]]:
    """
    For a specific mutli-part upload identified by the `file_id`, it returns an
    iterator to obtain download_urls.
    """
    while True:
        yield get_download_url(
            api_url=api_url,
            file_id=file_id,
        )


def start_multipart_upload(
    *, api_url: str, file_id: str, pubkey_path: Path
) -> Tuple[str, int]:
    """Try to initiate a multipart upload. If it fails, try to cancel the current upload
    can and then try to initiate a multipart upload again."""

    try:
        multipart_upload = initiate_multipart_upload(
            api_url=api_url,
            file_id=file_id,
            pubkey_path=pubkey_path,
        )
        return multipart_upload
    except exceptions.NoUploadPossibleError as error:
        file_metadata = get_file_metadata(api_url=api_url, file_id=file_id)
        upload_id = file_metadata["current_upload_id"]
        if upload_id is None:
            raise error

        patch_multipart_upload(
            api_url=api_url,
            upload_id=upload_id,
            upload_status=UploadStatus.CANCELLED,
        )

        multipart_upload = initiate_multipart_upload(
            api_url=api_url, file_id=file_id, pubkey_path=pubkey_path
        )

    except Exception as error:
        raise error

    return multipart_upload


def await_download_url(
    *,
    api_url: str,
    file_id: str,
    max_wait_time: int,
    message_display: AbstractMessageDisplay,
) -> Tuple[str, int]:
    """Wait until download URL can be generated.
    Returns a tuple with two elements:
        1. the download url
        2. the file size in bytes
    """

    # get the download_url, wait if needed
    wait_time = 0
    while wait_time < max_wait_time:
        try:
            response_body = get_download_url(
                api_url=api_url,
                file_id=file_id,
            )
        except exceptions.BadResponseCodeError as error:
            message_display.failure(
                "The request was invalid and returnd a wrong HTTP status code."
            )
            raise error
        except exceptions.RequestFailedError as error:
            message_display.failure("The request has failed.")
            raise error

        if response_body[0] is not None:
            download_url: str = response_body[0]
            file_size: int = response_body[1]
            return (download_url, file_size)

        retry_time: int = response_body[2]

        wait_time += retry_time
        message_display.display(
            f"File staging, will try to download again in {retry_time} seconds"
        )
        sleep(retry_time)

    raise exceptions.MaxWaitTimeExceededError(max_wait_time=max_wait_time)


def get_file_header_envelope(file_id: str, api_url: str, public_key: bytes) -> bytes:
    """
    Perform a RESTful API call to retrieve a file header envelope.
    Returns:
        The file header envelope (bytes object)
    """

    # encode public key in base64 (url-safe)
    public_key_encoded = base64.urlsafe_b64encode(public_key).decode("utf-8")

    # build url and headers
    url = f"{api_url}/objects/{file_id}/envelopes/{public_key_encoded}"

    headers = CaseInsensitiveDict(
        {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )

    # Make function call to get download url
    try:
        response = RequestsSession.get(url=url, headers=headers, timeout=TIMEOUT)
    except requests.exceptions.RequestException as request_error:
        raise exceptions.RequestFailedError(url=url) from request_error

    status_code = response.status_code

    if status_code == 200:
        return base64.b64decode(response.content)
    spec = {
        404: {
            "envelopeNotFoundError": lambda: exceptions.EnvelopeNotFoundError(
                file_id=file_id
            ),
            "noSuchObject": lambda: exceptions.FileNotRegisteredError(file_id=file_id),
        },
        500: {"externalAPIError": exceptions.ExternalApiError},
    }

    ResponseExceptionTranslator(spec=spec).handle(response=response)
    raise exceptions.BadResponseCodeError(url=url, response_code=status_code)
