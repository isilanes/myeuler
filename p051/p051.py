#--------------------------------------------------------------------#

def f1(max):
    #
    # WARNING: UNFINISHED!!
    #
    print("f1")

    # dict is a dictionary of:
    #
    # dict[length][last_digit] = some_list
    #
    # where some_list is the list of primes whose last digit is last_digit
    # and have length amount of digits. Only within each some_list
    # will we be able to form families. If two primes have different
    # amount of digits, obviously won't belong to the same family.
    # Also the last digit of any two members of a family must coincide.
    # Otherwise, it should be the digit that changes within the family,
    # and as it must be any 8 from [0..9], some of the "primes" would
    # not be prime, i.e. some would have to end in either 5 or an even
    # digit,
    # and as it must be any 8 from [0..9], some of the "primes" would
    # not be prime, i.e. some would have to end in either 5 or an even
    # digit..
    dict = {}

    # Sieve to find all primes up to max:
    composites = {}
    for mult in range(3,max,2):
        if not mult in composites:
            lp = len(str(mult))
            last_digit = str(mult)[-1]
            if not lp in dict:
                dict[lp] = {}

            if not last_digit in dict[lp]:
                dict[lp][last_digit] = []

            dict[lp][last_digit].append(mult)

            for i in range(mult*mult, max, 2*mult):
                composites[i] = True
    
    for length in sorted(dict.keys())[1:]: # ignore first one (length-1)
        print(length)
        for k,v in dict[length].items():
            print(k,dict[length][k])

#--------------------------------------------------------------------#

def f2(max):
    print("f2")

    # Sieve to find all primes up to max:
    composites = {} # dict of composite -> True
    primes = [2] # list of primes
    # dict of prime -> True (for faster searching than in array)
    dict = { 2 : True }
    for mult in range(3,max,2):
        if not mult in composites:
            # Store prime:
            primes.append(mult)
            dict[mult] = True

            # Sieve its multiples away:
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True
    
    # Check:
    for prime in primes[4:]: # ignore 1-digit primes
        print(prime)

#--------------------------------------------------------------------#

import timeit

# f1():
#t = timeit.Timer('f1(100)', "from __main__ import f1")
#t1 = t.timeit(number=1)

# f2():
t = timeit.Timer('f2(100)', "from __main__ import f2")
t2 = t.timeit(number=1)

print("\nTimes:\n")
print("t2 = {0:7.2f} s".format(t2)) # ~ s
