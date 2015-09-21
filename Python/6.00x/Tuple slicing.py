def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    n = 0
    rTup = ()
    while n < len(aTup):
        rTup += aTup[0+n:1+n] # or rTup += (aTup[n],)
        n += 2
    return rTup
    
def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]