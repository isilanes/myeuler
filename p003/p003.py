'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

#--------------------------------------------------------------------#

def f1(num0):
    factors = []
    
    num = num0
    max = num
    cum = 1
    
    last = 2
    while num > last:
        for i in range(last,max):
            while not num % i:
                factors.append(i)
                num = num/i
                cum = cum*i
                last = i
            if cum == num0:
                break

    return factors

#--------------------------------------------------------------------#

def f2(num0):

    factors = []

    # First, take out twos:
    num = num0
    while not num % 2: # while even
        factors.append(2)
        num = num/2

    # Then from 3 on:
    num = int(num)

    fac = 3
    while num > 1:
        fac = smallest(num, fac)
        num = int(num/fac)
        factors.append(fac)

    return factors

#--------------------------------------------------------------------#

def smallest(num, start):
    '''Returns smallest (thus, prime) subfactor of "num" that is
    larger than "start".'''
    import math

    for i in range(start,int(math.sqrt(num)+1),2):
        if not num % i: # divisible
            return i

    # If we reach thus far, there is no subfactor: number itself is prime:
    return num

#--------------------------------------------------------------------#

res = f2(600851475143)

print(res)
