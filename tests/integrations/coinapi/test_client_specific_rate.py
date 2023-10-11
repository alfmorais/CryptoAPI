import asyncio

import pytest

from cryptoapi.integrations.coinapi.client import CoinAPIClient


@pytest.mark.parametrize(
    "asset_id_base, asset_id_quote, expected_keys, expected_status_code",
    [
        ("BTC", "USD", ["time", "asset_id_base", "asset_id_quote", "rate"], 200),
        ("BTC", "BRL", ["time", "asset_id_base", "asset_id_quote", "rate"], 200),
        ("USD", "BRL", ["time", "asset_id_base", "asset_id_quote", "rate"], 200),
    ],
)
def test_client_specific_rate_success(
    asset_id_base,
    asset_id_quote,
    expected_keys,
    expected_status_code,
):
    client = CoinAPIClient()
    response = asyncio.run(client.specific_rate(asset_id_base, asset_id_quote))

    assert sorted(response[0].keys()) == sorted(expected_keys)
    assert response[0]["asset_id_base"] == asset_id_base
    assert response[0]["asset_id_quote"] == asset_id_quote
    assert response[1] == expected_status_code
