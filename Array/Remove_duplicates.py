def remove_duplicate(arr):
    arr2 = [0] * len(arr)
    curr = 0
    for i in range(len(arr)):
        if(arr2[curr - 1] != arr[i]):
            arr2[curr] = arr[i]
            curr += 1
    
    for i in range(curr):
        arr[i] = arr2[i]  
    return curr

print(remove_duplicate([10, 10, 20, 20,30])) 

