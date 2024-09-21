"""def power_of_2(n):
    if(n==0):
        return False
    while(n!=1):
        if(n%2!=0):
            return False
        n=n//2
    return True

print(power_of_2(4))"""


#brain Cunningham Algorithm
#tc=o(1)
def power_of_2(n):
    if(n==0):
        return 0
    
    return((n&(n-1))==0)
print(power_of_2(6))
