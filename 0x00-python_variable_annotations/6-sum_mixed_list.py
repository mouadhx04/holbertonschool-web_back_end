#!/usr/bin/env python3
"""type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum as a float"""
    return sum(mxd_lst)
