def bubble(arr):
    i=0
    while(i<len(arr)):
    #for i in range(0,len(arr)):
    
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        i+=1

    return arr
print(bubble([2,10,8,7,3]))

def bubble(arr):
    
    for i in range(0,len(arr)):
    
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr
print(bubble([2,10,8,7,3]))


#Optimized Solution
def bubble(arr):

    for i in range(0,len(arr)):

        swapped=False
    
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped=True

        if(swapped==False):
            break
        

    return arr
print(bubble([2,10,8,7,3]))



        
