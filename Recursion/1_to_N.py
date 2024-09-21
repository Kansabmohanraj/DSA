"""def One_n(n):
    if(n==0):
        return
    One_n(n-1)
    print(n)
 
One_n(4)
#TC=T(n-1)+0(n)=T(n)
#SC=0(n)"""

#In tail recursion methode
def One_n(n,k):

    if (n==0):
        return
    print(k)
    One_n(n-1,k+1)

One_n(10,1)


 
