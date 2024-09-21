
from prime import prime
def primeFactors(n):
    for i in range(2,n):
        if(prime(i)):
            while(n%i==0):
                print(i)
                n=n//i

primeFactors(10)