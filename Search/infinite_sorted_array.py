"""def infinite_sorted_array(arr,x):
    i=0
    while(True):

        if(arr[i]==x):
            return i
        if(arr[i]>x):
            return -1
        i+=1
    
print(infinite_sorted_array([1,3,6,8,9,10,90,440,4401],7))"""


def infinite_sorted_array(arr,x):
    if(arr[0]==x):
        return 0
    i=1
    while(arr[i]<x):
        i=i*2
        if(arr[i]==x):
            return i
    l=(i//2)+1
    r=i-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1

    return -1  
print(infinite_sorted_array([1, 3, 6, 8, 9, 10, 90, 440, 4401], 9)) 
    


