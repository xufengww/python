# -*- coding: utf-8 -*-
import time, functools

def log(str='default'):
    def decorator(fn):
        @functools.wraps(fn)
        def wraps(*args,**kw):
            print('begin call')
            ret = fn(*args,**kw)
            print('end call')

            return ret
        return wraps
    return decorator


@log
def f():
    print('666666666666')

@log('execute')
def fn():
    print('7777777777777777')
fn()