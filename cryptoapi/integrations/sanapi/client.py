import os
import aiohttp
import ujson


SANAPI_URL = os.environ["SANAPI_URL"]
SANAPI_TOKEN = os.environ["SANAPI_TOKEN"]


class SanAPIClient:

    def __init__(self, url: str = SANAPI_URL, token: str = SANAPI_TOKEN) -> None:
        self.url = url
        self.token = token
        self.headers = {"Authorization": self.token}

    async def crypto_information(self, body: dict) -> dict:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(url=self.url, json=body, headers=self.headers) as response:
                return await response.json(), response.status
