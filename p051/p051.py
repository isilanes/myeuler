#--------------------------------------------------------------------#

def f1(max):
    print("--- f1 ---")

    # Sieve to find all primes up to max:
    composites = {}
    primes = [2]
    pdict = {}
    for mult in range(3,max,2):
        if not mult in composites:
            # Log mult as prime:
            primes.append(mult)
            pdict[mult] = True

            # Sieve its multiples away:
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True
    
    # Check primes, one by one:
    longest = 0
    best = []
    for prime in primes[4:]: # ignore 1-digit ones
        for combo in f1_2(prime):
            a = f1_1(prime, combo, pdict)
            if len(a) > longest:
                longest = len(a)
                best = a
                print longest, best
                if longest > 7:
                    return

#--------------------------------------------------------------------#

def f1_1(prime, pos, pdict):
    '''
    Take a prime, and a position array pos, and return the family of 
    primes corresponding to it. Examples:

    prime = 113
    pos = [0,1]
    Check prime[0] and prime[1] coincide
    Check all xx3, for x in range(10) (that is 113, 223, 333, 443,
    553, 663, 773, 883 and 993) for primality (003 does not count).
    Return [113, 223, 443, 773, 883]

    prime = 1889
    pos = [0,2]
    As prime[0] (one) and prime[2] (eight) are not equal, return []

    '''

    family = []

    digits = [ int(x) for x in str(prime) ]

    for p in pos[1:]:
        if digits[p] != digits[pos[0]]: # not a valid position combo
            return []

    if pos[0] == 0:
        reps = range(1,10) # can't replace first digit with a zero
    else:
        reps = range(10)

    for rep in reps:
        d = digits[:]
        for i in pos:
            d[i] = rep
        res = int(''.join([str(x) for x in d]))
        if res in pdict:
            family.append(res)

    return family

#--------------------------------------------------------------------#

def f1_2(prime):
    '''
    Take a prime number, and return all valid digit-switch combos.
    A combo is an array of integers i, denoting ith digit in prime.
    For a combo to be valid, all ith digits must be equal among them,
    and the last digit can not be involved. Examples:

    prime = 11
    return [0] -> only combo

    prime = 113
    [0] is valid
    [1] is valid
    [0,1] is valid

    prime = 1889
    [0], [1], [2] -> valid
    [0,1] -> invalid
    [0,2] -> invalid
    [1,2] -> valid
    '''

    combos = []

    digits = [ int(x) for x in str(prime) ]
    n = len(digits)
    for subn in range(1,n):
        for combo in itertools.combinations(range(n-1), subn):
            ok = True
            for c in combo[1:]:
                if digits[c] != digits[combo[0]]: # combo not valid
                    ok = False
                    break
            if ok:
                combos.append(combo)

    return combos

#--------------------------------------------------------------------#

import timeit
import itertools

# f1():
t = timeit.Timer('f1(1000000)', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print(t1) # ~ s
