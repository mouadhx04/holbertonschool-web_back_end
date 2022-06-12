#!/usr/bin/env python3

"""tasks"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Test file for printing
    the correct output of
    the task_wait_n coroutine"""
    f = [
        task_wait_random(max_delay) for i in range(n)
    ]

    rs = []
    for x in asyncio.as_completed(f):
        r = await x
        rs.append(r)
    return rs
