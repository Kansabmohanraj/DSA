def count_digits(n):
    value=n
    count=0
    while(value>0):
        value=value//10
        count+=1

    return count

print(count_digits(145))
    



