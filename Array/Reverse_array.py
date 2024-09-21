def Reverse_array(arr):
    arr.reverse()
    return arr
print(Reverse_array([2,4,5,6]))

def Reverse_array(arr):
    arr2=[0]*(len(arr))
    for i in range (0,len(arr)):
        arr2[i]=arr[len(arr)-1-i]
    return arr2
print(Reverse_array([3,5,8]))

def reverse_array(arr):
    temp='0'
    for i in range(0,len(arr)//2):
        temp=arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=temp
    return arr
print(Reverse_array([3,5,8]))
print(reverse_array([3,5,8,7]))
