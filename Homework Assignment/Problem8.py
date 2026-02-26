def sortedarr(arr,target):
    for x in range(0,len(arr)):
        if arr[x]==target:
            print("target found at index",x)
        else :
            arr=arr.append(target)
            new_arr=arr.sort
            for y in range(0,len(new_arr)):
                if new_arr[y]==target:
                    print("target inserted at index",y)
sortedarr((1,2,3,6,8,9,11),3)
