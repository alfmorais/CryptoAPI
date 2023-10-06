import aiohttp


class SanAPIClient:

    @classmethod
    async def crypto_information(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        async with aiohttp.ClientSession() as session:
            return await session.post(url="", json={})
