def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    result = a * x ** 2 + b * x + c
    return result
    
a1 = 1.88, 
b1 = -4.89, 
c1 = -5.76, 
x1 = -0.72, 
a2 = -9.13, 
b2 = -1.49, 
c2 = 7.08, 
x2 = -2.08

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    result = evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)
    print result
