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

    # dictionary of digit -> list of primes not containing digit
    exclu = {
            '1': [2,3,5,7,],
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
    for ndig in range(2,8):
        for combo in it.combinations('123456789', ndig):
            num = ''.join(combo)
            num = int(num)
            if isprime(num):
                for si in '123456789':
                    if not si in combo:
                        exclu[si].append(num)
    num = 631
    s = str(num)
    pos = exclu[s[0]]
    for dig in s[1:]:
        pos = [ x for x in pos if x in exclu[dig] ]
    print num, pos
    for num2 in pos:
        s = str(num) + str(num2)
        pos = exclu[s[0]]
        for dig in s[1:]:
            pos = [ x for x in pos if x in exclu[dig] ]
        print num, num2, pos
        if not pos:
            if len(s) == 9:
                eureka
            else:
                this num, num2 not in solution

    return
    for k,v in exclu.items():
        for num in v:
            pos = exclu[str(num)[0]]
            for dig in str(num)[1:]:
                pos = [ x for x in pos if x in exclu[dig] ]
        return

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
