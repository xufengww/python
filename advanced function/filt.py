# -*- coding: utf-8 -*-
def is_palindrome(n):
    if not isinstance(n,int):
        raise TypeError('Type Error')
    else:
        return str(n) == str(n)[::-1]
