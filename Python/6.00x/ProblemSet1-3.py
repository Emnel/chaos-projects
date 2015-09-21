s = 'abcbcd'
longest = ''
x = 0
for char in s:
    y=0
    for char in s:
        if s[x+y:x+y+1] <= s[x+y+1:x+y+2]:
            y+=1
    if len(longest) < len(s[x:x+1+y]):
        longest = s[x:x+1+y]
    x+=1
print 'Longest substring in alphabetical order is: ' + longest       
        