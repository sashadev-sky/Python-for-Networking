import httpx
import asyncio


async def request_http1():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://www.google.es")
        print(response)
        print(response.text)
        print(response.http_version)  # HTTP/1.1

# request_http1()  # RuntimeWarning: coroutine 'request_http1' was never awaited
asyncio.run(request_http1())

