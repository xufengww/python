# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
         raise TypeError('bad operand type')
    elif not isinstance(b,(int,float)):
         raise TypeError('bad operand type')
    elif not isinstance(c,(int,float)):
         raise TypeError('bad operand type')

    if a==0:
     if b!=0:
        return -1*c/b
     else:
        return None

    deta = pow(b,2)-4*a*c

    if deta==0:
       return math.sqrt(c/a)
    elif deta<0:
        return None
    else:
        return (-b+math.sqrt(deta))/(2*a),(-b-math.sqrt(deta))/(2*a)