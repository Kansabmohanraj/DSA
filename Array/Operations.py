
def search(arr,x):
    for i in range(len(arr)):
        if(arr[i]==x):
            return i
    return -1

print(search([5,2,6,7],6))
print(search([5,8,9,0],2))



def insert_arr(arr,new,pos):
    index=pos-1
    arr2=[0]*(len(arr)+1)

    arr2[index]=new
    for i in range(0,len(arr)):
        arr2[i+1]=arr[i]

    return arr2
print(insert_arr([5,4,6,3,2],8,2))

def insert_new(arr,new,pos):
    index=pos-1
    arr2=[0]*(len(arr)+1)
    curr=0
    for i in range (0,len(arr)):
        arr2[i]=arr[i]

    for j in range(index,len(arr2)):
        curr=arr2[j]
        arr2[j]=new
        new=curr

    return arr2

print(insert_new([5,3,6,''],5,2))





