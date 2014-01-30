#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def isprime(num):
        '''
        Returns True if num is prime, False otherwise.
        '''

        if num == 1:
            return False

        if num in [2,3,5,7]:
            return True

        if num % 10 in [0,2,4,5,6,8]:
            return False

        i = 3
        while i*i < num:
            if not num % i:
                return False
            i += 2

        return True

    def s2pos(s, exclu):
        pos = exclu[s[0]]
        for dig in s[1:]:
            pos = [ x for x in pos if x in exclu[dig] ]
        return pos

    # dictionary of digit -> list of primes not containing digit
    exclu = {
            '1': [2,3,5,7],
            '2': [3,5,7],
            '3': [2,5,7],
            '4': [2,3,5,7],
            '5': [2,3,7],
            '6': [2,3,5,7],
            '7': [2,3,5],
            '8': [2,3,5,7],
            '9': [2,3,5,7]
            }

    # Harvest all primes that don't have repeated digits, 
    # and classify them into exclu above:
    primes = [2,3,5,7]
    for ndig in range(2,8):
        for combo in it.permutations('123456789', ndig):
            num = ''.join(combo)
            num = int(num)
            if isprime(num):
                primes.append(num)
                for si in '123456789':
                    if not si in combo:
                        exclu[si].append(num)

    valids = []
    for num1 in primes:
        s = str(num1)
        pos = s2pos(s, exclu)

        for num2 in pos:
            s = str(num1) + str(num2)
            pos = s2pos(s, exclu)
            if len(s) == 9:
                c = sorted([num1, num2])
                valids.append(tuple(c))

            for num3 in pos:
                s = str(num1) + str(num2) + str(num3)
                pos = s2pos(s, exclu)
                if len(s) == 9:
                    c = sorted([num1, num2, num3])
                    valids.append(tuple(c))

                for num4 in pos:
                    s = str(num1) + str(num2) + str(num3) + str(num4)
                    pos = s2pos(s, exclu)
                    if len(s) == 9:
                        c = sorted([num1, num2, num3, num4])
                        valids.append(tuple(c))

                    for num5 in pos:
                        s = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)
                        pos = s2pos(s, exclu)
                        if len(s) == 9:
                            c = sorted([num1, num2, num3, num4, num5])
                            valids.append(tuple(c))

                        for num6 in pos:
                            s = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6)
                            pos = s2pos(s, exclu)
                            if len(s) == 9:
                                c = sorted([num1, num2, num3, num4, num5, num6])
                                valids.append(tuple(c))

                            for num7 in pos:
                                s = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6)+str(num7)
                                pos = s2pos(s, exclu)
                                if len(s) == 9:
                                    c = sorted([num1, num2, num3, num4, num5, num6, num7])
                                    valids.append(tuple(c))

    valids = set(valids)
    for valid in valids:
        print valid
    print(len(valids))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
