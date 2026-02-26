def minJumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= n - 1:
                return jumps
                
    return -1 if current_end < n - 1 else jumps
minimum_jumps=minJumps([1,2,3,4,5,6,8,9])
print(f"minimum jumps:{minimum_jumps}")
