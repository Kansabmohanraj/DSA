def n_one(n):
    if(n==0):
        return
    print(n)
    n_one(n-1)
n_one(4)
#TC=T(n-1)+0(n)=T(n)
#SC=0(n)