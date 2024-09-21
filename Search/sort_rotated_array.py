def sort_rotate(arr,x):
    for i in range (0,len(arr)):
        if(arr[i]==x):
            return i
        
    return -1
print(sort_rotate([100,200,1000,10,20],10))

def sort_rotate(arr,x):
   
    l=0
    r=len(arr)-1
    while(l<=r):
        m=l+((r-l)//2)
        if(arr[m]==x):
            return m
        if(arr[l]<=arr[m]):
            if(arr[l] <=x<arr[m]):
                r=m-1
            l=m+1
        else:
            if(arr[m]<x<=arr[r]):
                l=m+1
            r=m-1
    return -1
print(sort_rotate([10,20,40,60,5,8],5))
print(sort_rotate([100,200,1000,10,20],10))



