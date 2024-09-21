def left_rotate_d(arr,d):
    count=0
    for i in range((d%len(arr)),len(arr)):
        temp=arr[count]
        arr[count]=arr[i]
        arr[i]=temp
        count+=1
    return arr
print(left_rotate_d([1,2,3,4,5,6],3))

"""def left_rotate_arr(arr, d) :
    arr2=[0]*(len(arr))
    for i in range((d%len(arr)),len(arr)):
        #2+1-3
        #3+1-3
        arr2[i-(d%len(arr))]= arr[i]
    print(arr2)
    counter=0
    for i in range(len(arr)-(d%len(arr)),len(arr)):
        arr2[i] = arr[counter]
        counter+=1
    return arr2
print(left_rotate_arr([1,2,3,4,5],5))"""

