"""def lcm(a,b):
    max_value=max(a,b)
    while(max_value%a!=0 or max_value%b!=0):
        max_value+=1
    return max_value
print(lcm(2,8))"""

#Efficient Solution
#a*b=gcd(a,b)*lcm(a,b)
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return(a*b)//gcd(a,b)

print(lcm(12,15))   

 