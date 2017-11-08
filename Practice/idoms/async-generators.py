#!/usr/bin/python3

async def ticker(delay, to):
    for i in range(to):
        yield await asyncio.sleep(delay)


import asyncio

async def test():
    return [i async for i in range(100) if i % 2]

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
