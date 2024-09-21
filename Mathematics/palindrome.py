def palindrome(n):
    value=n
    rev=0
    while(value!=0):
         
        lastd=value%10

        rev=rev*10+lastd;
        value=value//10;
         
        

    return (rev==n)

print(palindrome(121))
    
