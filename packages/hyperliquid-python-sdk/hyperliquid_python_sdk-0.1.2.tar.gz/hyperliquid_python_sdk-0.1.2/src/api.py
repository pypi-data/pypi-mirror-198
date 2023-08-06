import json
import logging
from json import JSONDecodeError
from typing import Dict, Any, cast

import requests

from src.utils.constants import MAINNET_API_URL
from src.utils.error import ClientError, ServerError
from src.utils.types import Json


class API:
    def __init__(
        self,
        base_url=None,
        show_header=False,
    ):
        self.base_url = MAINNET_API_URL
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
            }
        )

        if show_header is True:
            self.show_header = True

        self._logger = logging.getLogger(__name__)
        return

    def post(self, url_path: str, payload: Json = None) -> Json:
        if payload is None:
            payload = {}
        url = self.base_url + url_path

        response = self.session.post(url, json=payload)
        self._handle_exception(response)

        try:
            return cast(Dict[str, Any], response.json())
        except ValueError:
            return {"error": f"Could not parse JSON: {response.text}"}

    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(status_code, None, response.text, None, response.headers)
            error_data = None
            if "data" in err:
                error_data = err["data"]
            raise ClientError(status_code, err["code"], err["msg"], response.headers, error_data)
        raise ServerError(status_code, response.text)
