def f(s):
    return len(s) > 5
L = ['a', 'b', 'a', 'a', 'b', 'portal', 'tupet', 'abba']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    x = 0
    y = 0
    L1 = L[:]
    for s in L:
        if not f(s):
            del s
            y += 1
        x += 1
    print len(L)
    print L        