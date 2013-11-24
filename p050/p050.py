#--------------------------------------------------------------------#

def f1(max):
    print("f1")
    # Sieve to find all primes up to max:
    composites = {}
    primes = [2]
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)

            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    max_len = 1
    for istart in range(len(primes)):
        sum = primes[istart]
        i = istart
        while sum < max:
            i += 1
            try:
                sum += primes[i]
            except:
                break
            if sum in primes[i:]:
                length = i - istart + 1
                if length > max_len:
                    max_len = length
                    print(istart, length, sum)

#--------------------------------------------------------------------#

def f2(max):
    print("f2")
    import numpy as np

    # Sieve to find all primes up to max:
    composites = {}
    primes = [2]
    prime_dict = {}
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)
            prime_dict[mult] = True

            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    primes = np.array(primes)
    lp = len(primes)
    max_len = 1
    for istart in range(lp):
        if lp - istart < max_len:
            break
        for iend in range(istart,lp):
            s = sum(primes[istart:iend])
            if s > max:
                break
            if s in prime_dict:
                length = iend - istart
                if length > max_len:
                    max_len = length
                    print(istart, length, s)

#--------------------------------------------------------------------#

def f3(max):
    print("f3")
    import numpy as np

    # Sieve to find all primes up to max:
    composites = {}
    primes = [2]
    prime_dict = {}
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)
            prime_dict[mult] = True

            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    # Actual search for longest series:
    primes = np.array(primes)
    lp = len(primes)
    max_len = 1
    for istart in range(lp):
        s = sum(primes[istart:istart+max_len+1])
        if s > max:
            break

        for iend in range(istart+max_len,lp-1):
            s = sum(primes[istart:iend+1])
            if s > max:
                break

            if s in prime_dict:
                length = iend - istart + 1
                if length > max_len:
                    max_len = length
                    print(istart, length, s)

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1(1000000)', "from __main__ import f1")
t1 = t.timeit(number=1)

# f2():
t = timeit.Timer('f2(1000000)', "from __main__ import f2")
t2 = t.timeit(number=1)

# f3():
t = timeit.Timer('f3(1000000)', "from __main__ import f3")
t3 = t.timeit(number=1)

print("\nTimes:\n")
print(t1) # ~ 5000 s
print(t2) # ~  100 s
print(t3) # ~    1 s
