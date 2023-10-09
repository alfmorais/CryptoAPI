import pytest
import asyncio
from cryptoapi.integrations.sanapi.client import SanAPIClient


async def parameters_request():
    return [
        ({}, ({"errors": [{"message": "No query document supplied"}]}, 400)),
        (
            {
                "slug": "ethereum",
                "from": "2020-02-10T07:00:00Z",
                "to": "2020-03-10T07:00:00Z",
            },
            ({"errors": [{"message": "No query document supplied"}]}, 400),
        ),
        (
            {
                "from": "2020-02-10T07:00:00Z",
                "to": "2020-03-10T07:00:00Z",
                "interval": "1w",
            },
            ({"errors": [{"message": "No query document supplied"}]}, 400),
        ),
        (
            {
                "slug": "ethereum",
                "to": "2020-03-10T07:00:00Z",
                "interval": "1w",
            },
            ({"errors": [{"message": "No query document supplied"}]}, 400),
        ),
        (
            {
                "slug": "ethereum",
                "from": "2020-02-10T07:00:00Z",
                "interval": "1w",
            },
            ({"errors": [{"message": "No query document supplied"}]}, 400),
        ),
    ]


@pytest.mark.parametrize("payload,expected_response", asyncio.run(parameters_request()))
def test_sanapi_client_request_error(payload, expected_response):
    client = SanAPIClient()
    async_response = client.crypto_information(body=payload)

    assert expected_response == asyncio.run(async_response)


def test_sanapi_client_success():
    payload = {
        "slug": "dev_activity/ethereum",
        "from": "2020-02-10T07:00:00Z",
        "to": "2020-03-10T07:00:00Z",
        "interval": "1w",
    }
    expected_response = {}
    client = SanAPIClient()
    async_response = client.crypto_information(body=payload)

    assert expected_response == asyncio.run(async_response)
