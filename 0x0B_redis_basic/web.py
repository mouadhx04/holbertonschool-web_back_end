#!/usr/bin/env python3
''' web '''
from redis.client import Redis
import requests
from functools import wraps
from typing import Callable


red = Redis()


def count(method: Callable) -> Callable:
    ''' Count method '''
    @wraps(method)
    def wrapper(*args, **kwargs):
        ''' wrapper '''
        red.incr('count:' + args[0])
        p = red.get(args[0])
        if not p:
            p = method(*args, **kwargs)
            red.setex(args[0], 10, p)
        return p
    return wrapper


@count
def get_page(url: str) -> str:
    ''' Get '''
    req = requests.get(url)
    return req.text
