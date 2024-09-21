def Second_large_element(arr):
    x=max(arr)
    for i in range(0,len(arr)):
        if (x in arr):
            arr.remove(x)
        break
    #if(x in arr):
        #arr.remove(x)
    return arr.index(max(arr))  
print(Second_large_element([5,9,7,8,9,]))

    