"""def all_divisor( n): #100
    for i in range(1,n):#i=2
        if(n%i==0):#TRUE
            print(i)#2
        i+=1
    return i
print(all_divisor(45))"""

#efficient solution
def all_divisor(n):
    i=1
    while(i*i<n):
        if(n%i==0):
            print(i)
        i+=1    
    while(i>=1):        
        if(n%i==0):
            print(n//i)
        i-=1
                   
all_divisor(15)
