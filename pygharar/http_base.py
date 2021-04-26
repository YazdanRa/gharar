import logging
import time
from enum import Enum
from urllib.parse import urljoin

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, ReadTimeout

from .backoff import ExponentialBackoff

logger = logging.getLogger(__name__)

DEFAULT_BACKOFF = ExponentialBackoff(starting_delay=0.05, time_multiple=2)


class HttpCallMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class HttpProxy(object):
    def __init__(
            self, service_url, authorization_token=None, backoff=DEFAULT_BACKOFF, max_retry=0
    ):
        self._service_url = service_url
        self._backoff = backoff
        self._session = requests.Session()
        self._max_retry = max_retry
        if authorization_token is not None:
            self._session.headers["Authorization"] = f"Token {authorization_token}"

    def _call(self, path: str, method: HttpCallMethod, *args, **kwargs):
        tries = 0
        while True:
            try:
                response = self._session.request(
                    method=method,
                    url=urljoin(self._service_url, path),
                    *args,
                    **kwargs,
                )
                response.raise_for_status()
                return response
            except (ConnectionError, Timeout, HTTPError, ReadTimeout) as e:
                if tries >= self._max_retry:
                    raise e

                logger.warning(f"HTTP Error error_type: {type(e)} | error_message: {e}")
                time.sleep(self._backoff.get_delay_amount(tries))
                tries += 1

    def get(self, path, *args, **kwargs):
        return self._call(path=path, method=HttpCallMethod.GET, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        return self._call(path=path, method=HttpCallMethod.POST, *args, **kwargs)

    def put(self, path, *args, **kwargs):
        return self._call(path=path, method=HttpCallMethod.PUT, *args, **kwargs)

    def delete(self, path, *args, **kwargs):
        return self._call(path=path, method=HttpCallMethod.DELETE, *args, **kwargs)
