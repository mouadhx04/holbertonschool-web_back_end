#!/usr/bin/env python3

""" Let's execute multiple coroutines at the same time with async """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Test file for printing the correct output of the wait_n coroutine"""
    f = [
        wait_random(max_delay) for i in range(n)
    ]

    rs = []
    for x in asyncio.as_completed(f):
        r = await x
        rs.append(r)
    return rs
