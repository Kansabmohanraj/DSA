def leaders_array(arr):
    lead=arr[len(arr)-1]
    print(lead)
    for i in range(len(arr)-2,0,-1):
        if arr[i] > lead:
            lead = arr[i]
            print(lead)
    
leaders_array([7,10,4,3,6,5,2])




