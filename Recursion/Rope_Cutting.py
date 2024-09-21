def rope_cutting(n,a,b,c):
    if(n==0):
        return 0
    elif(n<0):
        return -1
    return max(1+rope_cutting(n-a,a,b,c), 1+rope_cutting(n-b,a,b,c),1+rope_cutting(n-c,a,b,c))
    
    
    
print(rope_cutting(5,2,5,1))
print(rope_cutting(23,12,9,11))
#TC=0(n)
#SC=0(n)
    