"""def merge(arr1,arr2):
    arr3 =arr1+arr2
    arr3.sort()

    return arr3
print(merge([1,2,3,4,5],[1,2,3,4]))"""


def merge(arr1,arr2):
    i=0
    j=0
    merged=[]

    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]<=arr2[j]):
            merged.append(arr1[i])

            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    while(i<len(arr1)):
        merged.append(arr1[i])

        i+=1

    while(j<len(arr2)):
        merged.append(arr2[j])

        j+=1

    return merged

print(merge([1,2,3,4,5],[1,2,3,4]))