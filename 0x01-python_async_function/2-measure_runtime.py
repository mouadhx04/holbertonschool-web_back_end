#!/usr/bin/env python3

"""Measure the runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time"""
    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - t0) / n)
