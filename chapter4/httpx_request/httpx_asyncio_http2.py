import httpx
import asyncio


async def resquest_http2():
	async with httpx.AsyncClient(http2=True) as client:
		response = await client.get("https://www.google.es")
		print(response)
		print(response.text)
		print(response.http_version)  # HTTP/2

asyncio.run(resquest_http2())

"""
Using the HTTP/2 version, which indicates that you can handle multiple requests
concurrently from a TCP stream.

Need to install the http2 extension using the following command:
>>> pip3 install httpx[http2]
"""
