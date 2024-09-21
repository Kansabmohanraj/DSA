"""def Sorted_not(arr):
    if(arr==sorted(arr)):
        return True
    return False

    
print(Sorted_not([3,4,8,3]))

def Sorted_not(arr):
    return arr == sorted(arr)

print(Sorted_not([3, 4, 8,5]))

def Sorted_not(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[i]):
                return False
            
    return True
print(Sorted_not([3,4,5]))   
print(Sorted_not([5,6,2,1,0]))  """  

def Sorted_not(arr):
    for i in range(0,len(arr)):

        for j in range(i+1,len(arr)):
        
            if(arr[j]<arr[i]):
                return False
            
    return True
print(Sorted_not([3,4,5]))   
print(Sorted_not([20,30,40,50,10]))

def Sorted_not(arr):
    for i in range(1,len(arr)):
        if(arr[i]<arr[i-1]):
            return False
    return True
print(Sorted_not([3,4,5]))   
print(Sorted_not([20,30,40,50,10])) 



