import aiohttp
import json
from config import CBR_API_URL

async def get_currency():
    async with aiohttp.ClientSession() as session:
        async with session.get(CBR_API_URL) as resp:
            text = await resp.text()
            return json.loads(text)