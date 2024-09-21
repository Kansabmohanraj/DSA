def count_1_arr(arr):
    count=0
    for i in range (0,len(arr)):
        if(arr[i]==1):
            count+=1
    
    return count
print(count_1_arr([0,0,1,1,1,1]))

def count_1_arr(arr):
    l=0
    r=len(arr)-1
    while(l<=r):
        m=l+((r-l)//2)
        if(arr[m]==0):
            l=m+1
        else:
            if(m==0 or arr[m-1]!=arr[m]):
                return (len(arr)-m)
            else:
                r=m-1

    return 0
print(count_1_arr([0,0,1,1,1,1]))
