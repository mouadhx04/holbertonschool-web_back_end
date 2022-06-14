#!/usr/bin/env python3

"""index_range"""


def index_range(page, page_size: int):
    """return a tuple of size two"""
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
