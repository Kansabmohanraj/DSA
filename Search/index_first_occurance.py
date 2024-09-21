#naive solution
"""def index_first(arr,target):
    for i in range(0,len(arr)):
        if(arr[i]==target):
            return i
    return -1
print(index_first([1,3,4,9,5,5],5))
#tc=0(len(arr))
#sc=0(len(arr))

#recursive solution
def index_first1(arr,target,l,r):
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
    
    return (index_first1(arr,target,l,r))
print(index_first1([1,3,4,9,5,5],5,0,5))"""
#tc=0(len(arr))
#sc=0(len(arr))

#iterative solution
def index_first2(arr,target):
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
print(index_first2([1,3,4,9,5,5],5))
#tc=0(len(arr))
#sc=0(len(arr))
