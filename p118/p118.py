#--------------------------------------------------------------------#

def f0():
    '''Slow and wrong?'''

    print("--- f0 ---")

    import itertools as it

    def isprime(num):
        '''Returns True if num is prime, False otherwise.'''

        if num == 1:
            return False

        if num in [2,3,5,7]:
            return True

        if num % 10 in [0,2,4,5,6,8]:
            return False

        i = 3
        while i*i < num+1:
            if not num % i:
                return False
            i += 2

        return True

    def s2pos(s, exclu):
        pos = exclu[s[0]]
        for dig in s[1:]:
            pos = [ x for x in pos if x in exclu[dig] ]
        return pos

    def are_compat(p1, p2):
        '''
        Return True if primes p1 and p2 are compatible (have no
        repeated digit), False otherwise.
        '''
        s2 = str(p2)
        for d1 in str(p1):
            if d1 in s2:
                return False
        return True


    # Harvest all primes that don't have repeated digits:
    primes = [2,3,5,7]
    for ndig in range(2,8):
        for combo in it.permutations('123456789', ndig):
            num = ''.join(combo)
            num = int(num)
            if isprime(num):
                primes.append(num)

    # Dict of prime -> list of primes compatible with it:
    com = {}
    for p1 in primes:
        com[p1] = []
        for p2 in primes:
            if are_compat(p1, p2):
                com[p1].append(p2)

    valids = []
    for p1 in primes:
      len1 = len(str(p1))
      for p2 in com[p1]:
        len2 = len(str(p2))
        if len1 + len2 == 9:
            c = sorted([p1,p2])
            valids.append(tuple(c))
            continue
        for p3 in com[p2]:
          if p3 in com[p1]:
            len3 = len(str(p3))
            if len1 + len2 + len3 == 9:
                c = sorted([p1,p2,p3])
                valids.append(tuple(c))
                continue
            for p4 in com[p3]:
              if p4 in com[p2] and p4 in com[p1]:
                len4 = len(str(p4))
                if len1 + len2 + len3 + len4 == 9:
                    c = sorted([p1,p2,p3,p4])
                    valids.append(tuple(c))
                    continue
                for p5 in com[p4]:
                  if p5 in com[p3] and p5 in com[p2] and p5 in com[p1]:
                    len5 = len(str(p5))
                    if len1 + len2 + len3 + len4 + len5 == 9:
                        c = sorted([p1,p2,p3,p4,p5])
                        valids.append(tuple(c))
                        continue
                    for p6 in com[p5]:
                      if p6 in com[p4] and p6 in com[p3] and p6 in com[p2] and p6 in com[p1]:
                        len6 = len(str(p6))
                        if len1 + len2 + len3 + len4 + len5 + len6 == 9:
                            c = sorted([p1,p2,p3,p4,p5,p6])
                            valids.append(tuple(c))
                            continue
                        for p7 in com[p6]:
                          if p7 in com[p5] and p7 in com[p4] and p7 in com[p3] and p7 in com[p2] and p7 in com[p1]:
                            len7 = len(str(p6))
                            if len1 + len2 + len3 + len4 + len5 + len6 + len7 == 9:
                                c = sorted([p1,p2,p3,p4,p5,p6])
                                valids.append(tuple(c))
                            else:
                                print c
                                return

    print len(valids)
    valids = set(valids)
    print len(valids)

def f1():
    print("--- f1 ---")

    import itertools as it

    def isprime(num):
        '''Returns True if num is prime, False otherwise.'''

        if num == 1:
            return False

        if num in [2,3,5,7]:
            return True

        if num % 10 in [0,2,4,5,6,8]:
            return False

        i = 3
        while i*i < num+1:
            if not num % i:
                return False
            i += 2

        return True
        

    valids = []
    for combo in it.permutations('123456789', 9):
        for c1 in range(1,9):
            num1 = int(''.join(combo[:c1]))
            if isprime(num1):
                # 2+ numbers:
                for c2 in range(c1+1,9):
                    num2 = int(''.join(combo[c1:c2]))
                    if isprime(num2):
                        # 3+ numbers:
                        for c3 in range(c2+1,9):
                            num3 = int(''.join(combo[c2:c3]))
                            if isprime(num3):
                                # 4+ numbers:
                                for c4 in range(c3+1,9):
                                    num4 = int(''.join(combo[c3:c4]))
                                    if isprime(num4):
                                        # 5+ numbers
                                        for c5 in range(c4+1,9):
                                            num5 = int(''.join(combo[c4:c5]))
                                            if isprime(num5):
                                                # Just 6 numbers:
                                                num6 = int(''.join(combo[c5:]))
                                                if isprime(num6):
                                                    c = sorted([num1,num2,num3,num4,num5,num6])
                                                    valids.append(tuple(c))
                                        # Just 5 numbers:
                                        num5 = int(''.join(combo[c4:]))
                                        if isprime(num5):
                                            c = sorted([num1,num2,num3,num4,num5])
                                            valids.append(tuple(c))
                                # Just 4 numbers:
                                num4 = int(''.join(combo[c3:]))
                                if isprime(num4):
                                    c = sorted([num1,num2,num3,num4])
                                    valids.append(tuple(c))
                        # Just 3 numbers:
                        num3 = int(''.join(combo[c2:]))
                        if isprime(num3):
                            c = sorted([num1,num2,num3])
                            valids.append(tuple(c))
                # Just 2 numbers:
                num2 = int(''.join(combo[c1:]))
                if isprime(num2):
                    c = sorted([num1,num2])
                    valids.append(tuple(c))

    res = len(set(valids))
    print(res)


#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1,2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 12.5 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
