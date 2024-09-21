def sq_root(x):
    i=1
    while(i*i<=x):
        i+=1
    return i-1
print(sq_root(4))

def sq_root(x):
    for i in range(x+1):
        if(i*i>x):
            return i-1
    return x
print(sq_root(20))

def sq_root(x):

    l=1
    r= x

    while l <= r:
        m = (l + r) // 2
        msq = m * m
        if msq == x:
            return m
        elif msq > x:
            r = m - 1
        else:
            l = m + 1
            
    return r

print(sq_root(17))

