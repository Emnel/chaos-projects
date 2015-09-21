def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr =='':
            return False
    elif aStr[len(aStr)/2: len(aStr)/2+1]  == char:
            return True
    elif aStr[len(aStr)/2: len(aStr)/2+1]  < char:
        return isIn(char, aStr[len(aStr)/2+1:])
    elif aStr[len(aStr)/2: len(aStr)/2+1]  > char:
        return isIn(char, aStr[:len(aStr)/2])
    