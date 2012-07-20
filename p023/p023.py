#-------------------------------------------------------------------------#

def f1(max=28123):
    
    abundants = {}

    # Sum of numbers that CAN'T be expressed as the sum of two 
    # abundant numbers:
    sum_cantbe = 1 # we will omit 1 below, which belongs here

    # Modified from p021:
    import math
    for i in range(2,max+1):
        divisors = {1:True}
        sum_divisors = 1
        for j in range(2,int(math.sqrt(i))+1):
            if not i % j:
                if not j in divisors:
                    sum_divisors += j
                    divisors[j] = True
                ij = int(i/j)
                if not ij in divisors:
                    sum_divisors += ij
                    divisors[ij] = True

        if sum_divisors > i:
            abundants[i] = True

        # Regardless of i being abundant, take advantage of the
        # loop and check if i is the sum of two abundant numbers.
        # Those two hypothetical abundant numbers will be smaller
        # than i itself, and thus already logged as such in 
        # previous cycles of the loop.
        canbe = False # can be expressed as the sum of two abundant numbers
        for j in range(12,i-11): # 12 is smallest abundant number
            if j in abundants:
                ij = i - j
                if ij in abundants:
                    canbe = True
                    break

        if not canbe:
            sum_cantbe += i

    return sum_cantbe

#-------------------------------------------------------------------------#

def f2(max=28123):
    
    abundants = {}
    ablist = []

    # Sum of numbers that CAN'T be expressed as the sum of two 
    # abundant numbers:
    sum_cantbe = 1 # we will omit 1 below, which belongs here

    # Modified from p021:
    import math
    for i in range(2,max+1):
        divisors = {1:True}
        sum_divisors = 1
        for j in range(2,int(math.sqrt(i))+1):
            if not i % j:
                if not j in divisors:
                    sum_divisors += j
                    divisors[j] = True
                ij = int(i/j)
                if not ij in divisors:
                    sum_divisors += ij
                    divisors[ij] = True

        if sum_divisors > i:
            abundants[i] = True
            ablist.append(i)

        # Regardless of i being abundant, take advantage of the
        # loop and check if i is the sum of two abundant numbers.
        # Those two hypothetical abundant numbers will be smaller
        # than i itself, and thus already logged as such in 
        # previous cycles of the loop.
        canbe = False # can be expressed as the sum of two abundant numbers
        for j in ablist:
            if j > i:
                break
            ij = i - j
            if ij in abundants:
                canbe = True
                break

        if not canbe:
            sum_cantbe += i

    return sum_cantbe

#-------------------------------------------------------------------------#

res = f2(28123)

print(res)
