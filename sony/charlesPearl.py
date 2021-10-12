# Question:
# you have a given range(b,c)
# give a sequence which number is not decreasing and in [b,c]
# the len(sequence) is from 1 to a, 1<=len(sequence)<=a
# Question: how many sequence can you give?

# given (b,c) = (8,9)
# a=1
# output:2
# explanation: (8) and (9)

# given (b,c) = (8,9)
# a=2
# output:5
# explanation: (8)  (9) (8,8) (8,9) (9,9)

# given (b,c) = (8,10)
# a=2
# output:9
# explanation: (8)  (9) (10)   (8,8) (8,9) (8,10) (9,9) (9,10) (10,10)

# given (b,c) = (0,9)
# a=10
# output: 184755
# explanation: too much to 


def solution(a,b,c):
    if a==1:
        return c-b+1
    cur_ans = 0
    for pivot in range(b,c+1):
        cur_ans += solution(a-1,pivot,c)
    return cur_ans

def main(a,b,c):
    res = 0
    while a>=1:
        res += solution(a,b,c)
        a-=1
    return res


def math_method(a,b,c):
    from math import comb
    length = c-b+1
    res = 0
    for number_num in range(1,length+1):
        # print("number_num:")
        # print(number_num)
        number_comb = 0
        if number_num>a:
            break
        for j in range(number_num-1, a):
            number_comb += comb(j, number_num-1)
        
        res+=comb(length,number_num)*number_comb
    return res


print("dfs:",main(2,8,9))
print("math:",math_method(2,8,9))
from time import time
s = time()
print("dfs:",main(10,0,20))
e = time()-s
print("time:",e)

s = time()
print("math:",math_method(10,0,20))
e = time()-s
print("time:",e)
