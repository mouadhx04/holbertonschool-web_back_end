#!/usr/bin/env python3
"""type-annotated function"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return values with the appropriate types """
    return [(i, len(i)) for i in lst]
