# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L)==0:
        return None,None
    
    Min = Max = L[0]

    for value in L:
        if Min>value:
            Min = value
        elif Max<value:
            Max = value
        
    return Min,Max