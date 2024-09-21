"""def gcd(a,b):
    min_value=min(a,b)
    while(a%min_value!=0 or b%min_value!=0):
        min_value-=1
    return min_value
print(gcd(100,200))  """          


#Eucludean Algorithm
"""def gcd(a,b):
    while(a!=b):
        if(a>b):
            a-=b
        else:
            b-=a
    return b
print(gcd(200,100))"""


#Euclidean Algorithm // optimized implimentation
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(0,30))

