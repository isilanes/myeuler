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

    while num > 1:
        fac = smallest(num)
        num = int(num/fac)
        factors.append(fac)

    return factors

#--------------------------------------------------------------------#

def smallest(num, start=3):
    '''Returns smallest (thus, prime) subfactor of "num" that is
    larger than "start".'''

    for i in range(start,int(num/2),2):
        if not num % i: # divisible
            return i

    # If we reach thus far, num is prime:
    return num

#--------------------------------------------------------------------#

for i in range(1000):
    #factors = f1(600851475143)
    factors = f2(600851475143)

print(factors[-1])
