import aiohttp
from config import CRYPTO_API_URL


async def get_top_crypto(limit=3):
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(
            CRYPTO_API_URL,
            params=params
        ) as resp:

            if resp.status != 200:
                return None

            return await resp.json()