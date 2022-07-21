from collections import abc
from io import BytesIO
from typing import (
    IO,
    Any,
    AnyStr,
    Dict,
    Mapping,
    Optional,
    Tuple,
    Union,
)
import zipfile

from pandas._typing import FilePathOrBuffer as FilePathOrBuffer

lzma = ...

def is_url(url) -> bool: ...
def validate_header_arg(header) -> None: ...
def stringify_path(
    filepath_or_buffer: FilePathOrBuffer[AnyStr],
) -> FilePathOrBuffer[AnyStr]: ...
def is_s3_url(url) -> bool: ...
def is_gcs_url(url) -> bool: ...
def urlopen(*args, **kwargs) -> IO: ...
def get_filepath_or_buffer(
    filepath_or_buffer: FilePathOrBuffer,
    encoding: Optional[str] = ...,
    compression: Optional[str] = ...,
    mode: Optional[str] = ...,
): ...
def file_path_to_url(path: str) -> str: ...
def get_compression_method(
    compression: Optional[Union[str, Mapping[str, str]]]
) -> Tuple[Optional[str], Dict[str, str]]: ...
def infer_compression(
    filepath_or_buffer: FilePathOrBuffer, compression: Optional[str]
) -> Optional[str]: ...
def get_handle(
    path_or_buf,
    mode: str,
    encoding=...,
    compression: Optional[Union[str, Mapping[str, Any]]] = ...,
    memory_map: bool = ...,
    is_text: bool = ...,
): ...

# ignore similar to what is in pandas source
class _BytesZipFile(zipfile.ZipFile, BytesIO):  # type: ignore[misc]
    archive_name = ...
    def __init__(
        self,
        file: FilePathOrBuffer,
        mode: str,
        archive_name: Optional[str] = ...,
        **kwargs,
    ) -> None: ...
    @property
    def closed(self) -> bool: ...

class _MMapWrapper(abc.Iterator):
    mmap = ...
    def __init__(self, f: IO) -> None: ...
    def __getattr__(self, name: str): ...
    def __iter__(self) -> _MMapWrapper: ...
    def __next__(self) -> str: ...
