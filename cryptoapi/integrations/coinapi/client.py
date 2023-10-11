import os
from collections.abc import Coroutine

import aiohttp

COINAPI_URL = os.environ["COINAPI_URL"]
COINAPI_TOKEN = os.environ["COINAPI_TOKEN"]


class CoinAPIClient:
    def __init__(self, url: str = COINAPI_URL, token: str = COINAPI_TOKEN) -> None:
        self.url = url
        self.token = token
        self.headers = {"X-CoinAPI-Key": self.token}

    async def __standard_get_request(self, url: str, headers: dict) -> Coroutine:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json(), response.status

    async def all_current_rates(self, asset_id_base: str) -> Coroutine:
        uri = "v1/exchangerate/{0}".format(asset_id_base)
        complete_url = "{0}{1}".format(self.url, uri)

        return await self.__standard_get_request(complete_url, self.headers)

    async def timeseries_data(self, asset_base: str, asset_quote: str) -> Coroutine:
        uri = "/v1/exchangerate/{0}/{1}/history".format(asset_base, asset_quote)
        complete_url = "{0}{1}".format(self.url, uri)

        return await self.__standard_get_request(complete_url, self.headers)

    async def timeseries_periods(self) -> Coroutine:
        uri = "/v1/exchangerate/history/periods"
        complete_url = "{0}{1}".format(self.url, uri)

        return await self.__standard_get_request(complete_url, self.headers)

    async def specific_rate(self, asset_id_base: str, asset_id_quote: str) -> Coroutine:
        uri = "v1/exchangerate/{0}/{1}".format(asset_id_base, asset_id_quote)
        complete_url = "{0}{1}".format(self.url, uri)

        return await self.__standard_get_request(complete_url, self.headers)
