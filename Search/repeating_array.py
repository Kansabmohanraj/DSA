def repeating_element(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]==arr[j]):
                return arr[i]
print(repeating_element([0,2,1,3,2,2]))
print(repeating_element([0,0]))
print(repeating_element([1,2,3,0,3,4,5]))
#TC =0(len(arr)^2)

def repeating_element(arr):
    arr.sort()
    for i in range(0,len(arr)):
        if(arr[i]==arr[i+1]):
            return arr[i]

print(repeating_element([0,2,1,3,2,2]))
print(repeating_element([0,0]))
print(repeating_element([1,2,3,0,3,4,5]))
#TC =0(len(arr))

def repeating_element(arr):
    



