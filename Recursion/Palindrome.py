"""def reverse(msg,i):
    if(i>=len(msg)):
        return ''
    return reverse(msg,i+1) + msg[i]"""
from Reverse_a_string import reverse
def palindrome(msg):
    if(msg==reverse(msg,0)):
        return True
    return False
print(palindrome('tamil'))
#TC=0(len(msg))
#SC=0(len(msg))