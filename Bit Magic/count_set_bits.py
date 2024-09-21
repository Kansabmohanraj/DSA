from bit_set_or_not import bit_set
"""def count_set(n):
    x=len(bin(n))
    count=0
    for i in range(1,x):
        if(bit_set(n,i)):
            count+=1
    return count  
print(count_set(5)) 
print(count_set(7))         
print(count_set(13))"""

"""def bit_set_or_not(n):
    count=0
    while(n>0):
        if(n%2==1):
            count+=1
        n=n//2
        
    return count
print(bit_set_or_not(7))"""

"""def bit_set_or_not(n):
    count=0
    while(n>0):
        count+=1
        n=n&(n-1)
    return count
print(bit_set_or_not(5))"""

def bit_set_or_not(n):
    count = 0
    while(n>0):
        n=n&(n-1)
        count+=1
    return count
print(bit_set_or_not(0)) 
     
