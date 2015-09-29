def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    aList = []
    for key in aDict.keys():
        theDict = aDict.copy()
        del theDict[key]
        if aDict.get(key) not in theDict.values():
            aList.append(key)
    return aList
    
        
