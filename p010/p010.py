def f1(max):
    primes = [2,3]
    i = primes[-1] + 2
    while i < max:
        is_prime = True
        for prime in primes:
            if prime * prime > i:
                break
            if not i % prime:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 2

    return sum(primes)

#------------------------------------------------------------------------------#

def f2(max):
    '''Try sieve of Eratostenes (I think), not "brute force".'''

    composites = {}
    sum = 2
    for mult in range(3,max,2):
        if not mult in composites:
            sum += mult
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    return sum

#------------------------------------------------------------------------------#

res = f2(2000000)

print(res)
