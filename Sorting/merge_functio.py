def merge_fun(arr,l,r):
    m=l+(r-l)//2

    n1=m-l+1
    n2=r-m
    left=[0]*(n1)
    right=[0]*(n2)

    for i in range(0,n1):
        left[i]=arr[l+i]
    for i in range(0,n2):
        right[i]=arr[m+i+1]
    
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if(left[i]<=right[j]):
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1

    while(i<n1):
        arr[k]=left[i]

        i+=1
        k+=1

    while(j<n2):
        arr[k]=right[j]
        j+=1
        k+=1

    return arr
#print(merge_fun([10,20,40,20,30],0,4))


