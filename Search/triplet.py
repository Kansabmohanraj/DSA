def triplet(arr,x):
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if(arr[i]+arr[j]+arr[k]==x):
                    return True
    return False
print(triplet([2,3,5,6,15],20))

def two_pointer(arr,x):
    i=0
    j=len(arr)-1
    while(i<j):
        if(arr[i]+arr[j]==x):
            return True
        elif(arr[i]+arr[j]>x):
            j-=1
        else:
            i+=1

    return False
def triplet(arr,x):
    for i in range(0,len(arr)-1):
        if(two_pointer(arr,x-arr[i])):
            return True
    return False
print(triplet([2,3,5,6,15],20))




