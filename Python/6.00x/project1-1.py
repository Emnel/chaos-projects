varA = 'aaa'
varB = 4
if type(varA or varB) == str:
    print "string involved"
elif varA > varB:
    print "bigger"
elif varA < varB:
    print "smaller"
else:
    print "equal"