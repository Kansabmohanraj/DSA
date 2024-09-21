"""def reverse(msg,i):
    if(i>=len(msg)):
        return
    reverse (msg,(i+1)) 
    print(msg[i], end="")

reverse("hello",0)
print(end="\n")"""

def reverse(msg,i):
    if(i==len(msg)):
        return ''
    return reverse(msg,i+1) + msg[i]
print(reverse("hello",0))
#TC=0(len(msg))
#SC=0(len(msg))