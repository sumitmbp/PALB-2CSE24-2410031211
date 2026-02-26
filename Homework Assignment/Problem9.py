def twoSum(nums, target):
    # Dictionary to store: {value: index}
    prev_map = {} 
    
    for i, n in enumerate(nums):
        diff = target - n
        # Check if the needed number has already been seen
        if diff in prev_map:
            return [prev_map[diff], i]
        
        # Store the current number and its index
        prev_map[n] = i
nums_list = [2, 7, 11, 15]
target_val = 9

indices = twoSum(nums_list, target_val)
print(f"Indices: {indices}")       
