# -*- coding: utf-8 -*-

def createCounter():
    i = 0
    def counter():
        nonlocal i 
        i += 1
        return i
   
    return counter