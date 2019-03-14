# -*- coding: utf-8 -*-
def normalize(name):
    if isinstance(name,str):
        name = name.title()
    else:
        raise TypeError('this isn\'t correct value')

    return name
