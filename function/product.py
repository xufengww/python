def product(*args):
    
    if(len(args)==0):#这一句一定要检测，因为有可能为product()，将无法检测到参数异常
        raise TypeError("TypeBad")
    
    ret = 1
    for x in args:
        if not isinstance(x,(int,float)):
            raise TypeError("TypeBad")
        ret *= x
    
    return ret
