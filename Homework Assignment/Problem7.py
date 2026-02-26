a=[2,3,-8,7,-1,2,3]
max=0
for i in range(len(a)):
    for j in range(i,len(a)):
        sum=0
        for k in range(i,j+1):
            sum+=a[k]
        if sum>max:
            max=sum
print(max)
