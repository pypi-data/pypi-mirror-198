from typing import Dict, Optional, Iterator, Generator
from dataclasses import dataclass, field
from abc import abstractmethod

import requests
from urllib.parse import urljoin
from base64 import b64encode

from .error import RequestError


@dataclass(frozen=True)
class Request:
    method: str
    url: str
    params: Dict[str, str] = field(default_factory=dict)
    headers: Dict[str, str] = field(default_factory=dict)
    content: Optional[bytes] = None


@dataclass(frozen=True)
class Response:
    status: int
    headers: Dict[str, str]
    content: Generator[bytes, None, None]

    def raise_for(self, status: int, content_type: Optional[str] = None) -> None:
        if self.status != status:
            self.content.close()
            raise RequestError(f"Response status {self.status}, expected {status}")
        if content_type is not None:
            ct: str = self.headers.get("Content-Type", "")
            if ct != content_type:
                self.content.close()
                raise RequestError(f"Response '{ct}', expected '{content_type}'")


class Authenticator:
    @abstractmethod
    def authenticate(self) -> Dict[str, str]:
        """Add authentication information to the given request headers, for example via Authorization or Cookie."""
        raise NotImplementedError

    @property
    @abstractmethod
    def username(self) -> str:
        raise NotImplementedError


class BasicAuthenticator(Authenticator):
    def __init__(self, username: str, password: str) -> None:
        self._username: str = username
        self._password: str = password

    def authenticate(self) -> Dict[str, str]:
        return {"Authorization": "Basic " + b64encode(f"{self._username}:{self._password}".encode()).decode()}

    @property
    def username(self) -> str:
        return self._username


class Requester:
    @abstractmethod
    def request(self, r: Request) -> Response:
        raise NotImplementedError

    @property
    @abstractmethod
    def username(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def base_url(self) -> str:
        raise NotImplementedError


class RequestsRequester(Requester):
    """Use the requests library for Request->Response on the API endpoint."""

    def __init__(self, base_url: str, authenticator: Authenticator, stream: bool = True, verify: bool = True) -> None:
        self._base_url: str = base_url
        self._authenticator: Authenticator = authenticator
        self._stream: bool = stream
        self._session: requests.Session = requests.Session()
        self._session.stream = stream
        self._session.verify = verify
        self._session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; nextcloud-tasks-api)"})

    def request(self, r: Request) -> Response:
        try:
            response: requests.Response = self._session.request(
                method=r.method.upper(),
                url=urljoin(self._base_url, r.url),
                params=r.params,
                headers={**r.headers, **self._authenticator.authenticate()},
                data=r.content,
            )
        except (requests.RequestException, ValueError) as e:
            raise RequestError(f"Cannot request '{r.url}': {str(e)}") from None

        return Response(status=response.status_code,
                        headers={k.title(): v for k, v in response.headers.items()},
                        content=self._response_stream(response))

    @classmethod
    def _response_stream(cls, response: requests.Response) -> Generator[bytes, None, None]:
        try:
            chunks: Iterator[bytes] = response.iter_content(chunk_size=None, decode_unicode=False)
            yield from chunks
        except requests.RequestException as e:
            raise RequestError(f"Cannot get response content: {str(e)}") from None
        finally:  # also for GeneratorExit
            response.close()

    @property
    def username(self) -> str:
        return self._authenticator.username

    @property
    def base_url(self) -> str:
        return self._base_url
