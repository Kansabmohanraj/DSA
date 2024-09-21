"""def index_last(arr,target):
    for i in range(len(arr)-1,0,-1):
        if(arr[i]==target):
            return i
    return -1
print(index_last([1,3,4,9,5,5],5))"""

def index_last1(arr, target):
    l=0
    r=len(arr)-1
    result=-1

    while l<=r:
        m=l+(r-l)//2
        if arr[m] < target:
            l=m+1
        elif arr[m] > target:
            r=m-1
        else:
            result = m
            l=m+1  

    return result

print(index_last1([1, 3, 4, 9, 5, 5], 5))  

"""def index_last2(arr, target, l, r):
    if (l>r):
        return -1

    m=l+(r-l)//2

    if arr[m] < target:
        l=m+1
    
    elif arr[m] > target:
        r=m-1
       
    else:
        if (m==r or arr[m+1] != target):
            return m
        else:
            return index_last2(arr, target, m+1, r)
    return -1"""

#print(index_last2([1, 3, 4, 5, 5, 5, 5], 5, 0, 6))
