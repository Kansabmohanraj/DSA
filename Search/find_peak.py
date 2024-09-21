def peak_element(arr):
    if(len(arr)==0):
        return arr[0]
    if(arr[0]>=arr[1]):
        return arr[0]
    if(arr[len(arr)-1]>=arr[len(arr)-2]):
        return arr[len(arr)-1]
    for i in range (1,len(arr)):
        if(arr[i-1]<arr[i]>arr[i+1]):
            return arr[i]
print(peak_element([5,10,20,15,7]))

def peak_element(arr):
    l=0
    r=len(arr)-1
    while(l<=r):
        m=l+((r-l)//2)
        if (m == 0 or arr[m-1] <= arr[m]) and (m==len(arr) - 1 or arr[m] >= arr[m + 1]):
            return arr[m]
        if (m>0 and arr[m-1] > arr[m]):
            r=m-1
        else:
            l=m+1
    return -1

print(peak_element([5,10,20,15,7]))

print(peak_element([80,70,60]))