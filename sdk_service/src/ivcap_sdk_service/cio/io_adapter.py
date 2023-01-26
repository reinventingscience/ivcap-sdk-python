from abc import ABC, abstractmethod
from typing import AnyStr, List, Callable, Optional, Sequence, Union
import io

#from ..logger import logger
from ..itypes import MetaDict, Url


class _IOBase(ABC):
    @property
    @abstractmethod
    def mode(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @property
    @abstractmethod
    def closed(self) -> bool:
        pass

    @abstractmethod
    def readable(self) -> bool:
        pass

    @abstractmethod
    def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
        pass

    @abstractmethod
    def seekable(self) -> bool:
        pass

    @abstractmethod
    def tell(self) -> int:
        pass

    @abstractmethod
    def writable(self) -> bool:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

class IOReadable(_IOBase):
    @abstractmethod
    def read(self, n: int = -1) -> AnyStr:
        pass

    @abstractmethod
    def readline(self, limit: int = -1) -> AnyStr:
        pass

    @abstractmethod
    def readlines(self, hint: int = -1) -> List[AnyStr]:
        pass

    @property
    @abstractmethod
    def path(self) -> str:
        pass

class IOWritable(_IOBase):
    @abstractmethod
    def write(self, s: AnyStr) -> int:
        pass

    @abstractmethod
    def writelines(self, lines: List[AnyStr]) -> None:
        pass

    @abstractmethod
    def truncate(self, size: int = None) -> int:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass


class IO_ReadWritable(IOReadable, IOWritable):
    pass

# class IOProxy(ABC):
#     """Represents a file-like object to read and write to"""

#     @abstractmethod
#     def open(self, mode: str, **kwargs) -> IO_ReadWritable:
#         """Return an IO object to read or write to depending on 'mode'"""

#     @abstractmethod
#     def close(self) -> None:
#         pass

#     @abstractmethod
#     def name(self) -> str:
#         """Returns name of underlying object"""
#         pass

OnCloseF = Callable[[Url], None]

class IOAdapter(ABC):

    @classmethod
    def create_cache(cls, cache_dir: str, cache_proxy_url: str):
        #return Cache(cache_dir=cacheDir, url_mapper=urlMapper)
        return None

    @abstractmethod
    def read_artifact(self, artifact_id: str, binary_content=True, no_caching=False, seekable=False) -> IOReadable:
        """Return a readable file-like object providing the content of an artifact

        Args:
            artifact_id (str): ID of artifact to read
            binary_content (bool, optional): If true content is expected to be of binary format otherwise text is expected. Defaults to True.
            no_caching (bool, optional): If true, content is not cached nor read from cache. Defaults to False.
            seekable (bool, optional): If true, returned readable should be seekable

        Returns:
            IOReadable: The content of the artifact as a file-like object
        """
        pass

    @abstractmethod
    def read_external(self, url: Url, binary_content=True, no_caching=False, seekable=False) -> IOReadable:
        """Return a readable file-like object providing the content of an external data item.

        Args:
            url (Url): URL of external object to read
            binary_content (bool, optional): If true content is expected to be of binary format otherwise text is expected. Defaults to True.
            no_caching (bool, optional): If set, content is not cached nor read from cache. Defaults to False.
            seekable (bool, optional): If true, returned readable should be seekable

        Returns:
            IOReadable: The content of the external data item as a file-like object
        """
        pass

    @abstractmethod
    def artifact_readable(self, artifact_id: str) -> bool:
        """Return true if artifact exists and is readable

        Args:
            artifact_id (str): ID of artifact

        Returns:
            bool: True if artifact can be read
        """
        pass

    @abstractmethod
    def write_artifact(
        self,
        mime_type: str, 
        name: Optional[str] = None,
        collection_name: Optional[str] = None,
        metadata: Optional[Union[MetaDict, Sequence[MetaDict]]] = None, 
        seekable=False,
        on_close: Optional[OnCloseF] = None
    ) -> IOWritable:
        """Returns a IOWritable to create a new artifact. It needs to be closed
        in order to be persisted. If `on_close` is provided it is called with the 
        artifactID.

        Args:
            mime_type (str): _description_
            name (Optional[str], optional): Optional name. Defaults to None.
            collection_name (Optional[str], optional): Optional collection name. Defaults to None.
            metadata (Optional[MetaDict | List[MetaDict]], optional): Key/value pairs (or list of key/value pairs) to add as metadata. Defaults to {}.
            seekable (bool, optional): If true, writable should be seekable (needed for NetCDF). Defaults to False.
            on_close (Optional[OnCloseF], optional): Called with assigned artifact ID. Defaults to None.

        Returns:
            IOWritable: A file-like object to write deliver artifact content - needs to be closed
        """
        pass

    # @abstractmethod
    # def get_fd(self, name: str, metadata: Dict[str, any] = {}) -> Tuple[Union[str, BinaryIO], str]:
    #     """
    #     Create and return a file handle and path

    #     Parameters
    #     ----------
    #     name: str
    #         Filename used to save data, file path is set by adapter
    #     metadata: None
    #         Unused in this Adapter

    #     Returns
    #     -------
    #         file_obj: capy.io.io_adapter.WritableProxyFile
    #             A thin wrapper of io.IOBase and used in same manner

    #     """
    #     pass

    # @abstractmethod
    # def exists(self, name: str) -> Tuple[bool, str]:
    #     pass

    # @abstractmethod
    # def readable(self, name: str) -> bool:
    #     pass
    
    # @abstractmethod
    # def read(self, name: str, seekable=False, use_cache_proxy=True) -> IOProxy:
    #     pass



