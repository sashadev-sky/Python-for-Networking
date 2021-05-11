import httpx
import trio

results = {}


async def fetch_result(client, url, results):
    print(url)
    results[url] = await client.get(url)


async def main_parallel_requests():
	async with httpx.AsyncClient(http2=True) as client:
		async with trio.open_nursery() as nursey:
			for i in range(2000, 2020):
				url = f"https://en.wikipedia.org/wiki/{i}"
				nursey.start_soon(fetch_result, client, url, results)

trio.run(main_parallel_requests)
print(results)

"""
$ p3 httpx_http2_trio.py
https://en.wikipedia.org/wiki/2000
https://en.wikipedia.org/wiki/2001
https://en.wikipedia.org/wiki/2002
https://en.wikipedia.org/wiki/2003
https://en.wikipedia.org/wiki/2004
https://en.wikipedia.org/wiki/2005
https://en.wikipedia.org/wiki/2006
https://en.wikipedia.org/wiki/2007
https://en.wikipedia.org/wiki/2008
https://en.wikipedia.org/wiki/2009
https://en.wikipedia.org/wiki/2010
https://en.wikipedia.org/wiki/2011
https://en.wikipedia.org/wiki/2012
https://en.wikipedia.org/wiki/2013
https://en.wikipedia.org/wiki/2014
https://en.wikipedia.org/wiki/2015
https://en.wikipedia.org/wiki/2016
https://en.wikipedia.org/wiki/2017
https://en.wikipedia.org/wiki/2018
https://en.wikipedia.org/wiki/2019
{'https://en.wikipedia.org/wiki/2000': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2002': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2003': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2004': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2005': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2006': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2007': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2008': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2011': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2012': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2013': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2016': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2001': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2010': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2014': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2015': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2017': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2009': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2018': <Response [200 OK]>, 'https://en.wikipedia.org/wiki/2019': <Response [200 OK]>}
"""