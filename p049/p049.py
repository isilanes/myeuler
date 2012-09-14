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

    # The withdigits dict contains the info we need:
    solutions = []
    for k, v in withdigits.items():
        lv = len(v)
        if lv > 2:
            diffs = {}
            for i in range(lv):
                for j in range(i+1,lv):
                    diff12 = v[j] - v[i]
                    for k in range(j+1,lv):
                        diff23 = v[k] - v[j]
                        if diff23 > diff12:
                            break

                        if diff23 == diff12:
                            diffs[diff12] = [i, j, k]
                            solutions.append([v[i], v[j], v[k]])

    return solutions

#--------------------------------------------------------------------#

for solution in f1():
    print(solution)
