import json
import logging

from ..confighelper import ConfigHelper
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import HTTPHeaders
from typing import Any


class Storage:
    def __init__(self, config: ConfigHelper) -> None:
        self.server = config.get_server()
        self.storage_server = config.get('storage_server', None)
        self.client = AsyncHTTPClient()
        if self.storage_server is None:
            raise config.error("storage_server is required")

    async def create_dir(self, path: str, headers: HTTPHeaders) -> Any:
        token: str = headers.get("Authorization").split(" ")[1]
        server_path: str = "/server/files/directory"
        request = HTTPRequest(
            f"{self.storage_server}{server_path}", 
            "POST", 
            body=json.dumps({
                "path": path,
            }),
            headers={
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json",
            },
        )
        try: 
            result = await self.client.fetch(request)
            return json.loads(result.body)
        except Exception as e:
            logging.info("Can't create a new folder: %s", e)
            return None


def load_component(config: ConfigHelper) -> Storage:
    return Storage(config)
