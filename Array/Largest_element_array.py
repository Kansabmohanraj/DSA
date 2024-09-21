def largest_array(arr):
    large=-1
    for i in range(0,len(arr)):
        if(arr[i]>large):
            #large=arr[i]
            largest_index=i
            large=arr[i]
    return large, largest_index
print(largest_array([5,10,10,9]))

def largest_array(arr):
    large=max(arr)
    large1=arr.index(large)

    return arr.index(max(arr))
print(largest_array([5,10,10,9,15]))

def largest_array(arr):
    return arr.index(max(arr))
print(largest_array([5,7,9,2,0,1]))

