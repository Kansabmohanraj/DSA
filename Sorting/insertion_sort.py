def insertion(arr):
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]

        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=temp

    return arr
print(insertion([20,5,40,60,10,30]))