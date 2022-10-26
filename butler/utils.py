import json
import mimetypes
import os
from io import FileIO
from typing import TypeVar

from butler.generated.types import Response


# Basic error handling for HTTP failure statuses
class HttpException(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(f"status code {status_code}, {message}")


T = TypeVar("T")


def verify_response_or_raise(response: Response[T]) -> T:
    if response.status_code >= 200 and response.status_code < 400:
        return response.parsed
    else:
        message = None
        try:
            e = json.loads(response.content)
            message = e.get("message") if isinstance(e, dict) else None
        finally:
            raise HttpException(response.status_code, message or "unknown error")


# Utils for inferring file name and mime type for a local file
def infer_file_name(f: FileIO) -> str:
    return os.path.basename(f.name)


def infer_mime_type(file_name: str) -> str:
    mime_type = mimetypes.guess_type(file_name)[0]
    if mime_type is None:
        raise RuntimeError(f"could not infer mime type for file {file_name}, please specify mime type manually")
    return mime_type


# Empty class for bypassing improper codegen for cases that have
# both multipart/form-data and application/json requests
class EmptyJsonBody:
    def to_dict(self):
        return {}
