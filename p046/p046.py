def f1(max):
    import math

    primes = []
    primed = {}
    composites = {}
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)
            primed[mult] = True
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True
        else:
            # Check if Goldbach's conjecture holds:
            gold = False
            for prime in primes:
                pj = math.sqrt((mult-prime)/2.0)
                if not pj % 1:
                    gold = True
                    break

            if not gold:
                return mult

#-------------------------------------------------------------------------#

res = f1(10000)
print(res)
