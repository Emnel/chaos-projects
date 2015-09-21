def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    if exp == 0:
        return 1
    else:
        while exp > 0:
            result *= base
            exp -= 1
        return result
        
        
def iterPower1(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    if exp == 0:
        return result
    else:
        for value in range(exp):
            result *= base
        return result
        