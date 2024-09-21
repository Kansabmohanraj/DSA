def power_set(s):
    n=len(s)
    psize=2**n
    for i in range(0,(psize)):
        out=""
        for j in range(0,n):
            if(i&(1<<j))!=0:
                out+=s[j]
        print(out)
power_set("abc")