s = 'aabbvbvafgdvcxvzerwerDFDFZxdXcb'
vowels = ( 'a', 'e', 'u', 'o', 'i')
count = 0
for char in s:
    if char in vowels:
        count += 1
print 'Number of vowels: %d' % count        
        