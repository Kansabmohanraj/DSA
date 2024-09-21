"""def compute(x,n):
    count=1
    if(n==0):
        return 1
    for i in range(0,n):
        if(i<n):
            count=count*x
    i+=1
    return count
print(compute(5,0))"""

def power(x,n):
    if(n==0):
        return 1
    temp=power(x,n//2)
    temp=temp*temp
    remp=power(x,n-1)*x
    if(n%2==0):
        return  temp
    else:
        return remp
    
print(power(2,3))