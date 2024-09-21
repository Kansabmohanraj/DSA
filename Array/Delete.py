def delete(arr,x):
    Id=False
    for i in range(0,len(arr)):
        if(arr[i]==x):
            Id=True
        if(Id==True and i!=len(arr)-1):

            arr[i]=arr[i+1]
        if(i==len(arr)-1):
            arr[i]="_"
    return arr
print(delete([5,3,6,7],3))



def delete(arr, x):
    if x in arr:
        arr.remove(x)
    return arr

print(delete([1, 5, 7, 3], 5))



