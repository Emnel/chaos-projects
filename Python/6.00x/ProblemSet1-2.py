s = 'bobobobobobbobsdfsdf'
count = 0
x = 0
for char in s:
    if s[x:x+3] == 'bob':
        count+=1
    print s[x:x+3]
    x+=1
print 'Number of times bob occurs is: %d' % count        
        