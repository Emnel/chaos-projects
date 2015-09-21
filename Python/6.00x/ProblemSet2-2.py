annualInterestRate  = 0.2
balance = 4773
monthlyPayment = 0
theBalance = balance
while theBalance > 0:
    theBalance = balance
    monthlyPayment += 10
    for month in range(12):
        theBalance = (theBalance - monthlyPayment)*(1.0+annualInterestRate/12.0)
print "Lowest Payment: %d" % monthlyPayment