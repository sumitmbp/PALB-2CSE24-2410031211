def minMax(arr):
  '''for empty array'''
    if not arr:
        return None
    '''assigning value to begin comparison'''
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
            
    return [min, max]
