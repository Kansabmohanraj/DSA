def median_two(arr1,arr2):
    arr3=arr1+arr2
    arr3.sort()
    if((len(arr3)%2)==1):
        return arr3[len(arr3)//2]
    else:
         return (arr3[len(arr3)//2-1]+arr3[len(arr3)//2])/2

print(median_two([1,2,4],[1,2,3]))