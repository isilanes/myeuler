'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

#-------------------------------------------------------------------------#

def f1(max):
    
    # Find proper divisors of all numbers requested, and log their sum:
    sumdivisors = {}
    for i in range(2,max):
        divisors = [1]
        for j in range(2,int(i/2)+1):
            if not i % j:
                divisors.append(j)

        sd = sum(divisors)
        sumdivisors[i] = sd

    # Find amicable pairs:
    amicable_sum = 0
    amicable = {}
    for num, sd in sumdivisors.items():
        if sd != num and sd in sumdivisors and sumdivisors[sd] == num and not sd in amicable:
            amicable[num] = sd
            amicable_sum += sd + num

    return amicable_sum

#-------------------------------------------------------------------------#

def f2(max):
    import math
    
    # Find proper divisors of all numbers requested, and log their sum:
    sumdivisors = {}
    for i in range(2,max):
        divisors = [1]
        for j in range(2, int(math.sqrt(i))+1):
            if not i % j:
                divisors.append(j)
                divisors.append(int(i/j))

        sd = sum(divisors)
        sumdivisors[i] = sd

    # Find amicable pairs:
    amicable_sum = 0
    amicable = {}
    for num, sd in sumdivisors.items():
        if sd != num and sd in sumdivisors and sumdivisors[sd] == num and not sd in amicable:
            amicable[num] = sd
            amicable_sum += sd + num

    return amicable_sum

#-------------------------------------------------------------------------#

res = f2(10000)

print(res)
