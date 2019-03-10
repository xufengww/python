# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    if n== 2:
        print(a,'-->',b)
        print(a,'-->',c)
        print(b,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)