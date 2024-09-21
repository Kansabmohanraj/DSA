def merge_sort_divide(arr):
    if len(arr) == 1 : #2
        print(arr)
        return arr
    l=0
    r=len(arr)-1
    m = (l + r) // 2
    left_arr = arr[l:m + 1]
    right_arr = arr[m + 1:r + 1]
    """mid = (len(arr))//2 # 1
    left_arr = [0]*(len(arr)-mid) #1
    right_arr = [0]*(mid) #1
    j = 0
    left_index = 0 #0
    while (left_index < len(arr)) : 
        if (left_index<mid) :
            left_arr[left_index] = arr[left_index]
        elif (j<len(right_arr)):
            right_arr[j] = arr[left_index]
            j+=1
        left_index+=1"""
    return merge_sort_conquer(merge_sort_divide(left_arr), merge_sort_divide(right_arr))

def merge_sort_conquer(left_arr, right_arr) :
    res=[0]*(len(left_arr) + len(right_arr))
    
    i=0
    j=0
    res_index=0
    while (i<len(left_arr) and j < len(right_arr)) :
        if ((right_arr[j] > left_arr[i])) :
            res[res_index] = left_arr[i]
            i+=1
        else:
            res[res_index] = right_arr[j]
            j+=1
        res_index+=1
    while (i<len(left_arr)) :
        res[res_index] = left_arr[i]
        i+=1
    while (j<len(right_arr)) :
        res[res_index] = right_arr[j]
        j+=1
    return res

print(merge_sort_divide([38,27,43,10,55,60]))
#print (merge_sort_conquer([27,38], [10,43]))
