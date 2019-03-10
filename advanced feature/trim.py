# -*- coding: utf-8 -*-
def trim(s):
    while s!='' and s[:1]==' ':
        s = s[1:]
    while s!='' and s[-1]==' ':
        s = s[:-1]
    return s


#一种很好的解决办法：
#def trim(s):
#    if s == '':
#        return s
#    if s[0] == ' ':
#        return trim(s[1:])
#    if s[-1] == ' ':
#        return trim(s[:-1])
#    return s
