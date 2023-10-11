import asyncio

import pytest

from cryptoapi.integrations.coinapi.client import CoinAPIClient


@pytest.mark.parametrize(
    "asset_id_base, first_collum_keys, second_collum_keys, expected_status_code",
    [
        ("BTC", ["asset_id_base", "rates"], ["time", "asset_id_quote", "rate"], 200),
        ("USD", ["asset_id_base", "rates"], ["time", "asset_id_quote", "rate"], 200),
        ("BRL", ["asset_id_base", "rates"], ["time", "asset_id_quote", "rate"], 200),
        ("EUR", ["asset_id_base", "rates"], ["time", "asset_id_quote", "rate"], 200),
    ],
)
def test_client_all_current_rates_success(
    asset_id_base, first_collum_keys, second_collum_keys, expected_status_code
):
    client = CoinAPIClient()
    response = asyncio.run(client.all_current_rates(asset_id_base))

    assert response[0]["asset_id_base"] == asset_id_base
    assert sorted(response[0].keys()) == sorted(first_collum_keys)
    assert sorted(response[0]["rates"][0].keys()) == sorted(second_collum_keys)
    assert response[1] == expected_status_code
