def bit_set(n,i):
    #i-=1
    x=1<<(i-1)
    if(n&x!=0):
        return True
    return False

"""print(bit_set(5,1))
print(bit_set(8,2))
print(bit_set(0,3))"""