def f1():
    # Sieve to find all primes up to 10000 (all 4-digit ones inside):
    max = 10000
    composites = {}
    primes = [2]
    withdigits = {} # sorted digits -> prime with them
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)
            digits = ''.join(sorted(str(mult)))
            if digits in withdigits:
                withdigits[digits].append(mult)
            else:
                withdigits[digits] = [mult]

            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    # The withdigits contains the info we need:
    for k, v in withdigits.items():
        if len(v) > 2:
            print(v, v[2] - v[1])
            #if v[2] - v[1] == v[1] - v[0]:
            #    return [k, v]

#--------------------------------------------------------------------#

res = f1()
print(res)
