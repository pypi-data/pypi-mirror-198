# -*- coding: utf-8 -*-
"""Utils used across multiple commands and/or apis"""
from typing import Iterator


def get_recursively(obj: dict | str, key: str) -> Iterator:
    """Recursively get values in a dict for a given key

    Args:
        obj (dict | str): Either dict type object or string
        key (str): Key to search for

    Yields:
        Iterator: Iterator for further recursive search or desired values
    """

    if isinstance(obj, str):
        return

    try:
        for k, val in obj.items():
            if k == key:
                yield val
            else:
                yield from get_recursively(val, key)
    except AttributeError:
        try:
            for val in obj:
                yield from get_recursively(val, key)
        except TypeError:
            pass
