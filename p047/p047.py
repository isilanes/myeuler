def f1():
    i = 13
    while True:
        delta = 1
        if factor_amount(i) == 4:
            delta += 1
            if factor_amount(i+1) == 4:
                delta += 1
                if factor_amount(i+2) == 4:
                    delta += 1
                    if factor_amount(i+3) == 4:
                        return i

        i += delta

#--------------------------------------------------------------------#

def factor_amount(compo):
    '''Return the number of unique factors of composite number compo.'''

    factors = []
    diff_factors = {}

    # First, take out twos:
    num = compo
    while not num % 2: # while even
        factors.append(2)
        diff_factors[2] = True
        num = num/2

    # Then from 3 on:
    num = int(num)

    fac = 3
    while num > 1:
        fac = smallest(num, fac)
        num = int(num/fac)
        factors.append(fac)
        diff_factors[fac] = True

    return len(diff_factors)

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

res = f1()
print(res)
