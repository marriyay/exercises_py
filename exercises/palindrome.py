import re

__all__ = ["is_palindrome"]


def is_palindrome(string: str) -> bool:
    forward = ''.join(re.findall(r'[a-z]+', string.lower()))
    backward = forward[::-1]
    return forward == backward
