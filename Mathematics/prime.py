"""def prime(n):
    if (n==1):
        return False
    for i in range (2,(n//2)+1):
        if(n%i==0):
            return False
    return True
print(prime(4))"""


#Effective Method
"""def prime(n):
    if n < 2:
        return False
    i = 2
    while(i*i <= n):
        if(n % i == 0):
            return False
        i += 1
    return True
print(prime(11))"""


#More Effective Method
def prime(n):
    if(n==1):
        return False
    if(n==2 and n==3):
        return True
    if(n%2==0 and n%3==0):
        return False
    i=5
    while(i*i<=n):
        if(n%i==0 and n%(i+2)==0):
            return False
        i+=6
    return True
(prime(11))
    
