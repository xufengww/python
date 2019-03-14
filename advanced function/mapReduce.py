# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    [s1,s2] = s.split('.',2)
    def str2num(c):
        return int(c)
    return reduce(lambda x,y:x*10+y,map(str2num,s1))+reduce(lambda x,y:x*10+y,map(str2num,s2))/pow(10,len(s2))


print(str2float('123.456'))