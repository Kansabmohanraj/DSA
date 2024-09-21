"""def count_occurance(arr,target):
    count=0
    for i in range (0,len(arr)):
        if(arr[i]==target):
            count+=1
        
    return count
print(count_occurance([10,30],20))"""


#in 0(log len(arr))time

def binary_search_first(arr, target):
    left=0 
    right =len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def binary_search_last(arr, target):
    left=0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def count_occurance(arr, target):
    first = binary_search_first(arr, target)
    if first == -1:
        return 0  # Target is not present
    last = binary_search_last(arr, target)
    return (last - first + 1)

# Example usage
print(count_occurance([10, 20, 20, 30], 20)) 
