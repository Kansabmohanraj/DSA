from one_odd_occuring import one_odd_occuring

def two_odd_ocuuring(numitha):
    count = 0 
    result = one_odd_occuring(numitha)

    pos_first_set_bit = 0
    while(result>0):
        result=result&(result-1)
    #len_result=len(bin(result))
    #for i in range(1,#len_result):
        #if(bit_set(result,i)):
        pos_first_set_bit+=1
        break
    set_1=0
    set_2=0
    for j in (numitha):
        if((j&(1<<pos_first_set_bit)!=0)):
            set_1=set_1^j
        else:
            set_2=set_2^j

    return set_1,set_2

print(two_odd_ocuuring([5,6,10,6,10,6,3,3]))

    
