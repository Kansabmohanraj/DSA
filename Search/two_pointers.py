def two_point(arr,x):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)-1):
            if(arr[i]+arr[j]==x):
                return True
    return False
print(two_point([2,5,8,12,30],17))
print(two_point([3,8,13,18],14))

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
print(two_point([2,5,8,12,30],17))
print(two_point([3,8,13,18],14))

