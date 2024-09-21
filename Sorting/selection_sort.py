def selection(arr):
    arr2=[0]*(len(arr))

    
    for i in range(0,len(arr)):
        arr2[i]= min(arr)
        arr.remove(min(arr))
    return arr2
print(selection([3,2,7,1]))


def selection(arr):
    n = len(arr)
    
    for i in range(n):
        minid = i
        for j in range(i + 1, n):
            if arr[j] < arr[minid]:
                minid = j

        temp=arr[i]
        arr[i] = arr[minid]
        arr[minid]=temp
    
    return arr

print(selection([3, 2, 7, 1]))





