annualInterestRate  = 0.2
monthlyPaymentRate  = 0.04
balance = 4842
monthlyPayment = 0
month = 0
totalPaid = 0

while month < 12:
    monthlyPayment = balance * monthlyPaymentRate
    balance = (balance - monthlyPayment)*(1.0+annualInterestRate/12.0)
    totalPaid += monthlyPayment
    month += 1
    print "Month %d" % month
    print "Minimum monthly payment: %r" % round(monthlyPayment, 2)
    print "Remaining balance: %r" % round(balance, 2)
print "Total paid: %r" % round(totalPaid, 2)
print "Remaining balance: %r" % round(balance, 2)
