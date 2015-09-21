annualInterestRate  = 0.2
balance = 320000
low = balance/12
high = (balance*(1.0+annualInterestRate/12.0)**12)/12
theBalance = balance

while abs(theBalance) > 0.01:
    theBalance = balance
    monthlyPayment = (high+low)/2
    for month in range(12):
        theBalance = (theBalance - monthlyPayment)*(1.0+annualInterestRate/12.0)
    if theBalance > 0:
        low = monthlyPayment
    else:
        high = monthlyPayment
print "Lowest Payment: %r" % round(monthlyPayment, 2)