#!/usr/bin/env python3
"""
exercise
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' counts the times a function is
        being called
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper '''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    ''' store the history of inputs
        and outputs for a particular function.
    '''
    call_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper '''
        str_input = str(args)
        self._redis.rpush(call_key + ':inputs', str_input)
        self._redis.rpush(
            call_key + ':outputs',
            method(self, *args, **kwargs)
        )
        return method(self, *args, **kwargs)
    return wrapper


def replay(fn: Callable) -> str:
    ''' display the history of
        calls of a particular function.
    '''
    data = fn.__qualname__
    inputs = f"{data}:inputs"
    outputs = f"{data}:outputs"
    redis_ = fn.__self__._redis
    input_redis = redis_.lrange(inputs, 0, -1)
    count = redis_.lrange(outputs, 0, -1)
    Q = fn.__self__._redis.get(data).decode('utf-8')
    print(f"{data} was called {Q} times:")
    for i, j in zip(input_redis, count):
        print(f"{data}(*{i.decode('utf-8')}) -> {j.decode('utf-8')}")


class Cache:
    ''' Cache '''
    def __init__(self):
        ''' Init '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Stores a key '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, data: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        ''' returns stored data '''
        if data:
            fn_data = self._redis.get(data)
            if fn:
                return fn(fn_data)
            else:
                return fn_data

    def get_str(self, data: bytes) -> str:
        ''' parametrize Cache.get with the correct
            conversion function
        '''
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        ''' parametrize Cache.get with the correct
            conversion function.
        '''
        return int(data)
