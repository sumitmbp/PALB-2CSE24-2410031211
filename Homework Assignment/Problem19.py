def find_triplet(arr, target):
    n = len(arr)
    # 1. Sort the array
    arr.sort()

    # 2. Iterate through the array
    for i in range(n - 2):
        # Initialize two pointers
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return True # Triplet found
            
            elif current_sum < target:
                left += 1 # Need a larger sum
            else:
                right -= 1 # Need a smaller sum
                
    return False # No triplet found
