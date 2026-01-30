def findKthSmallest(arr, k):
  '''sorting the array would give nlogn complexity.'''
    arr.sort()
'''since sorted the k-1th place will hold the biggest value'''
    return arr[k-1]
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
result = findKthSmallest(arr, k)
print(f"The {k}th smallest element is:", result)
