import asyncio
from snusbase import SnusbaseClient

snusbase = SnusbaseClient("API_KEY")

async def main():
    results = await snusbase.ip_lookup("1.1.1.1")
    print(results)

asyncio.run(main())
