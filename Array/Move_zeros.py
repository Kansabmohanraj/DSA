def move_zeros(arr):
    for i in range(0,len(arr)):
        if(arr[i]==0):
            for j in range((i),(len(arr)-1)):
                    arr[j]=arr[j+1]
            arr[len(arr)-1]=0

    return arr
print(move_zeros([10,0,3,0,20]))

def move_zeros(arr):
    for i in range(0,len(arr)):
        if(arr[i]==0):
            for j in range(i+1,len(arr)):
                if(arr[j]!=0):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
                    i+=1
    return arr
print(move_zeros([10,0,0,20,0,80]))  


def move_zeros(arr):
    count = 0
    for i in range (0,len(arr)):

        if(arr[i]!=0):
            temp = arr[i]
            arr[i] = arr[count]
            arr[count] = temp

            count+=1
    return arr
print(move_zeros([10,5,0,0,8,0,9,0]))
                         
               
