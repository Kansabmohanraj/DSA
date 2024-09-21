def binary_search(arr,target):
    l=0
    r=len(arr)-1
    while(l<=r):
        m=l+((r-l)//2)
        if(arr[m]==target):
            return m
        if(arr[m]<target):
            l=m+1
        else:
            r=m-1
    return -1
print(binary_search([2,6,8,10,10],10))

def binary_search_recursion(arr,target,l,r):
    if(l>=r):
        return -1
    m=l+((r-l)//2)
    if(arr[m]==target):
        return m
    if(arr[m]<target):

        l=m+1
    #if(arr[m]>targert):
    else:
        r=m-1
    
    return (binary_search_recursion(arr,target,l,r))
print(binary_search_recursion([4,5,6,7,12],16,0,4))