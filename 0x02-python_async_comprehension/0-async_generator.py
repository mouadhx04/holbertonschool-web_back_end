#!/usr/bin/env python3

"""Write a coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loop 10 times and
    wait 1 second each time asynchronous
    then yield a random number between 0,10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
