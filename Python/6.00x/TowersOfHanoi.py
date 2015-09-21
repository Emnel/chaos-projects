def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
        
Watch him actually perform the algorithm. When he moves 3 at once he wasn't performing the algorithm, but trying to explain how to think about recursion and breaking a problem into smaller problems + a base case. So with a 4 disc tower, it initially breaks down into moving a 3 disc set to the spare, then moving 1 disc to the destination, and finally moving the 3 disc set from the spare to the destination. With recursion the smaller problem keeps breaking down into smaller problems, until all that is left is base case problems occurring.
So, you end up with something like:
def Hanoi(size, source, target, spare):
    if size == 1:
       print "move %s to %s" % (source, target)
    else:
       hanoi(size - 1, source, spare, target)
       hanoi(1, source , target, spare)
       hanoi(size - 1, spare, target, source)
The example where he moved 3 at once it equates to:
hanoi(4, 's', 't', 'sp')
     hanoi(3, 's', 'sp', 't')  <== he moves stack of 3 off to spare
     hanoi(1, 's', 't', 'sp')  <== so he has simple problem of moving only 1 to target
     hanoi(3, 'sp', 't', 's')  <== then figures out how to get the 3 stack there
To see how it completely breaks down for a smaller tower (size 3):
hanoi(3, 's', 't', 'p')
    hanoi(2, 's', 'p', 't')
         hanoi(1, 's', 't', 'p') -- "move s to t"
         hanoi(1, 's', 'p', 't') -- "move s to p"
         hanoi(1, 't', 'p', 's') -- "move t to p"
    hanoi(1, 's', 't', 'p')      -- "move s to t"
    hanoi(2, 'p', 't', 's')
         hanoi(1, 'p', 's', 't') -- "move p to s"
         hanoi(1, 'p', 't', 's') -- "move p to t"
         hanoi(1, 's', 't', 'p') -- "move s to t"
        