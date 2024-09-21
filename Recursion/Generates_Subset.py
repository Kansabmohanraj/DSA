def subset(set, curr , i):
    #length=len(set)
    if(i>=len(set)):
        print(curr)
        return
    
    subset(set,curr+'',i+1)
    subset(set,curr+set[i],i+1)
    #print(curr)

subset("ab",'',0)

    