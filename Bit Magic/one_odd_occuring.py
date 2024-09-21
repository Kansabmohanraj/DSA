
def one_odd_occuring(nums):
    count = 0
    for i in nums:
        count = count ^ i
    return count
#print(one_odd_occuring([5,1,6,1,5,5]))


0^5^1^6^1^5
0^5^5^1^1^6
0^0^0^6
0^0^6
0^6
6
