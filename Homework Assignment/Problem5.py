#for this simple iteration will do the job 
def largest(arr):
  max=arr[0]
  for i in range(1,len(arr)):
    if max <arr[i]:
      max=arr[i]
    else:
      continue
  return max
