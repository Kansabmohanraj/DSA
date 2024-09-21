def factorial(n):
    value=n
    fact=1
    not_exit=0
    if n<0:
        return not_exit
    elif (n==1 or n==0):
        return 1
    else:
        for i in range(2,value+1):
            fact=fact*i

        return fact
print(factorial(2))        

