#!/usr/bin/env python3
"""web file"""
from typing import Callable
import requests
import redis
from functools import wraps

redis_object = redis.Redis()


def count_req(method: Callable) -> Callable:
    """counr request"""

    @wraps(method)
    def wrapper(link):
        """call back func"""
        redis_object.incr("count:{}".format(link))
        ch = redis_object.get("cached:{}".format(link))
        if ch:
            return ch.decode('utf-8')
        f = method(link)
        redis_object.setex("cached:{}".format(link), 10, f)
        return f

    return wrapper


@count_req
def get_page(url: str) -> str:
    """get_page"""
    request = requests.get(url)
    return request.text
