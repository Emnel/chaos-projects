def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = ( 'a', 'e', 'i', 'o' , 'u')
    char = char.lower()
    if char in vowels:
        return True
    else:
        return False

