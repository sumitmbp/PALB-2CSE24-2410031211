def findUnion(a, b):
    '''combine the array'''
    c = a + b
    
    '''Sort the array, here complexity becomes O(nlogn)'''
    c.sort()
    
    '''iterate to remove the duplicate'''
     #handling the empty array
    if not c:
        return []
    
    result = [c[0]]
    for i in range(1, len(c)):
        #here comparing the next element with previous element 
        if c[i] != c[i-1]:
          #adding element that do not match in result array
            result.append(c[i])
            
    return result

#overall complexity will be nlogn for sorting then n for iteration then 1 for a+b, so overall highest complexity would come out to be nlogn maybe!
