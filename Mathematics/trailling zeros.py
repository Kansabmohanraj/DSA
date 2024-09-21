"""def trailling_zero(n):
    value=n
    fact=1
    count=0
    for i in range(2,value+1):
        fact=fact*i


    while(fact%10==0):
        fact = fact//10
        count+=1    

    return count
print(trailling_zero(125))"""  
def trailling_zero(n):

    count=0
    prime_factor =1

    #count+=n//5 #### number//prime_factor==1
    #count+=n//25###
    while(n//prime_factor>1):
        
        prime_factor*=5
        count+=n//prime_factor
    

    
    return count
print(trailling_zero(124))    