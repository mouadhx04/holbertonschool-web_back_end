#!/usr/bin/env python3
""" a type-annotated function """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """function safely_get_value"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
