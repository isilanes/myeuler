def f1():
    # Sieve to find all primes up to max. If not enough, increase max.
    max = 1000000
    composites = {}
    primes = [2]
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    # Check those primes for truncability:
    truncatables = []
    for prime in primes:
        # (In)valid digits:
        # 0: invalid (can't be first, if not first yields multiple of 10 at some truncation
        # 1: valid except if first or last (not prime)
        # 2: valid only if first, else yields even num at some truncation
        # 3, 7: valid
        # 4, 6, 8: invalid. If first, not prime. If not, yield even num at some truncation
        # 5: valid only if first, else yields multiple of 5 at some truncation
        # 9: valid, except if first or last

        sp = str(prime)
        if not '0' in sp:
            if not '1' == sp[0] and not '1' == sp[-1]:
                if not '2' in sp[1:]:
                    if not '4' in sp:
                        if not '5' in sp[1:]:
                            if not '6' in sp:
                                if not '8' in sp:
                                    istruncatable = True

                                    # Truncate from right to left:
                                    sp = sp[:-1]
                                    while sp:
                                        p = int(sp)
                                        if p in composites:
                                            istruncatable = False
                                            break
                                        sp = sp[:-1]

                                    # Truncate from right to left:
                                    sp = str(prime)
                                    if istruncatable:
                                        sp = sp[1:]
                                        while sp:
                                            p = int(sp)
                                            if p in composites:
                                                istruncatable = False
                                                break
                                            sp = sp[1:]

                                        if istruncatable:
                                            truncatables.append(prime)

    return sum(truncatables[4:]) # take out the 1-digit primes

#-------------------------------------------------------------------------#

res = f1()
print(res)
