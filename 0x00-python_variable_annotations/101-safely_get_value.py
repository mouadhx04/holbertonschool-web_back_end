#!/usr/bin/env python3
""" type-annotated function """

from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'),
                                    None]) -> Union[Any,
                                                    TypeVar('T')]:
    """ function safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
