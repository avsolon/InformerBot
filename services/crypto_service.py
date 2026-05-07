from config import CRYPTO_API_URL, CRYPTO_SEARCH_URL, CRYPTO_PRICE_URL
from utils.http_client import HTTPClient


async def get_top_crypto(limit=3):
    session = await HTTPClient.get_session()

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "price_change_percentage": "24h"
    }

    async with session.get(CRYPTO_API_URL, params=params) as resp:
        if resp.status != 200:
            return []

        return await resp.json()


async def search_coin(query: str):
    session = await HTTPClient.get_session()

    # search coin
    async with session.get(CRYPTO_SEARCH_URL, params={"query": query}) as resp:
        data = await resp.json()

    coins = data.get("coins", [])
    if not coins:
        return None

    coin = coins[0]

    coin_id = coin["id"]

    # price
    async with session.get(
        CRYPTO_PRICE_URL,
        params={
            "ids": coin_id,
            "vs_currencies": "usd",
            "include_24hr_change": "true"
        }
    ) as resp:
        price = await resp.json()

    if coin_id not in price:
        return None

    p = price[coin_id]

    return {
        "name": coin["name"],
        "symbol": coin["symbol"].upper(),
        "price": p["usd"],
        "change": p.get("usd_24h_change", 0)
    }

# import aiohttp
# from config import CRYPTO_API_URL
#
#
# async def get_top_crypto(limit=3):
#     params = {
#         "vs_currency": "usd",
#         "order": "market_cap_desc",
#         "per_page": limit,
#         "page": 1,
#         "sparkline": "false",
#         "price_change_percentage": "24h"
#     }
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get(
#             CRYPTO_API_URL,
#             params=params
#         ) as resp:
#
#             if resp.status != 200:
#                 return None
#
#             return await resp.json()