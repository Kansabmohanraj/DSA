def sum_digits(n):
    if(n<=9):
        return n
    return sum_digits(n//10) + n%10
print(sum_digits(231))

#TC=0(d)
#SC=0(d)