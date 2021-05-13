import time
import asyncio
from typing import Coroutine

async def wait(delay: int) -> Coroutine:
    print(f'wait for {delay} seconds at {time.strftime("%X")}')
    await asyncio.sleep(delay)
    print(f'waited for {delay} seconds at {time.strftime("%X")}')

"""
Lower-level Imlementation
`loop = asyncio.get_event_loop()
`loop.run_until_complete(wait(2))
"""

asyncio.run(wait(2))

"""
$ p3 event_loop.py
wait for 2 seconds at 22:49:56
waited for 2 seconds at 22:49:58
"""

