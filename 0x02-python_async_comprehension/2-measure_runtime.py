#!/usr/bin/env python3

"""Run time for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ asyncio.gather"""
    t0 = time.time()
    rs = [async_comprehension() for i in range(4)]
    await asyncio.gather(*rs)
    return time.time() - t0
