#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math
    import itertools as it

    def isprime(num):
        '''
        Returns True if num is prime, False otherwise.
        '''

        # Only odd numbers are fed to this function, so no need
        # to check num % 2:
        for i in range(3,int(math.sqrt(num))+2,2):
            if not num % i:
                return False

        return True

    # Number of digits we check for (10 in p111):
    N = 10

    # TS4d  =       273700 (     31 ms)

    TSNd = 0
    for d in range(10):
        nd = N-1
        others = [0,1,2,3,4,5,6,7,8,9]
        others.remove(d)
        while True:
            SNd = 0

            nothers = N - nd
            permus = []
            for combo in it.product(others, repeat=nothers):
                for permu in it.permutations((d,)*nd+combo, N):
                    if permu[-1] in [1,3,7,9]: # else, can't be prime
                        if permu[0] != 0: # else, has N-1 digits or less
                            num = ''.join([ str(x) for x in permu ])
                            num = int(num)
                            permus.append(num)
            
            permus = set(permus)
            for num in permus:
                if isprime(num):
                    SNd += num

            if SNd == 0:
                nd -= 1
            else:
                TSNd += SNd
                break

    print(TSNd)

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    def isprime(num):
        '''
        Returns True if num is prime, False otherwise.
        '''

        # Only odd numbers, no need to check num % 2:
        i = 3
        while i*i < num:
            if not num % i:
                return False
            i += 2

        return True

    def d0():
        '''
        Return sum of all 10-digit primes that contain 8 zeros. 
        No 9-zero prime could exist, as that would mean the number 
        either starts with 0 (then has 9 digits) or ends in zero
        (then is even).
        '''

        tot = 0

        # Only possible situation for 2 non-zero digits is
        # first AND last digits:
        for i in [1,2,3,4,5,6,7,9]:
            for j in [1,3,7,9]:
                num = i*10**9 + j
                if isprime(num):
                    tot += num
        return tot

    def d1():
        '''
        Return sum of all 10-digit primes that contain 9 ones.
        '''

        tot = 0

        # Non-one is first digit:
        for i in [2,3,4,5,6,7,8,9]:
            num = i*10**9 + 111111111
            if isprime(num):
                tot += num

        # Non-one is digit 2 to 9 from left:
        for pos in range(2,10):
            for i in [0,2,3,4,5,6,7,8,9]:
                num = i*10**(10-pos) + 1111111111 - 10**(10-pos)
                if isprime(num):
                    tot += num
        
        # Non-one is last digit:
        for i in [3,7,9]:
            num = i + 1111111110
            if isprime(num):
                tot += num

        return tot

    def d2():
        '''
        Return sum of all 10-digit primes that contain 8 twos.
        No 10-digit prime exists with 9 twos. The only option
        would be a 2222222220 + {0..9}, and none of them
        are prime. Recall one of the two non-two digits must
        be the last one (if not, number would be even).
        '''

        tot = 0

        # Non-twos are first and last digits:
        for i in [1,3,4,5,6,7,8,9]:
            for j in [1,3,7,9]:
                num = i*10**9+j + 222222220
                if isprime(num):
                    tot += num

        # Non-twos are last digit and one of second to ninth from left:
        for pos in range(2,10):
            for i in [0,1,3,4,5,6,7,8,9]:
                for j in [1,3,7,9]:
                    num = i*10**(10-pos) + j + 2222222220 - 2*10**(10-pos)
                    if isprime(num):
                        tot += num

        return tot

    def d3():
        '''
        Return sum of all 10-digit primes that contain 9 threes. Recall
        that the tenth digit can be neither 0, nor 6, nor 9 (nor 3,
        obviously), as then the sum of digits would be 3*k, and then
        3 would be a factor of the number (and thus, it wouldn't be prime).
        '''

        tot = 0

        # Non-three digit is first to ninth from left:
        for pos in range(1,10):
            for i in [1,2,4,5,7,8]:
                num = i*10**(10-pos) + 3333333333 - 3*10**(10-pos)
                if isprime(num):
                    tot += num

        # Non-three digit is last one:
        for i in [1,7]:
            num = i + 3333333330
            if isprime(num):
                tot += num

        return tot

    def d4():
        '''
        Return sum of all 10-digit primes that contain 9 fours. Recall
        that the non-four digit must be the last one, lest the number
        be even.
        '''

        tot = 0

        for i in [1,3,7,9]:
            num = i + 4444444440
            if isprime(num):
                tot += num

        return tot

    def d5():
        '''
        Return sum of all 10-digit primes that contain 9 fives. Recall
        that the non-four digit must be the last one, lest the number
        be 5*k.
        '''

        tot = 0

        for i in [1,3,7,9]:
            num = i + 5555555550
            if isprime(num):
                tot += num

        return tot

    def d6():
        '''
        Return sum of all 10-digit primes that contain 9 sixes. Recall
        that the non-four digit must be the last one, lest the number
        be even.
        '''

        tot = 0

        for i in [1,3,7,9]:
            num = i + 6666666660
            if isprime(num):
                tot += num

        return tot

    def d7():
        '''
        Return sum of all 10-digit primes that contain 9 sevens.
        '''

        tot = 0

        # Non-seven is first digit:
        for i in [1,2,3,4,5,6,8,9]:
            num = i*10**9 + 777777777
            if isprime(num):
                tot += num

        # Non-seven is second to ninth digit from left:
        for pos in range(2,10):
            for i in [0,1,2,3,4,5,6,8,9]:
                num = i*10**(10-pos) + 7777777777 - 7*10**(10-pos)
                if isprime(num):
                    tot += num
        
        # Non-seven is last digit:
        for i in [1,3,9]:
            num = i + 7777777770
            if isprime(num):
                tot += num

        return tot

    def d8():
        '''
        Return sum of all 10-digit primes that contain 8 eights. There
        are no 9-eight 10-digit primes, as the non-eight would have to
        be the last digit (lest the number be even), and none of the
        resulting numbers are prime. Recall, likewise, that in the 8 eight
        primes the last number will always be non-eight.
        '''

        tot = 0

        # Non-eights are first and last digits:
        for i in [1,2,3,4,5,6,7,9]:
            for j in [1,3,7,9]:
                num = i*10**9+j + 888888880
                if isprime(num):
                    tot += num

        # Non-eights are last digit and second to ninth digit from left:
        for pos in range(2,10):
            for i in [0,1,2,3,4,5,6,7,9]:
                for j in [1,3,7,9]:
                    num = i*10**(10-pos) + j + 8888888880 - 8*10**(10-pos)
                    if isprime(num):
                        tot += num

        return tot

    def d9():
        '''
        Return sum of all 10-digit primes that contain 9 nines. Recall
        that the tenth digit can be neither 0, nor 3, nor 3 (nor 9,
        obviously), as then the sum of digits would be 3*k, and then
        3 would be a factor of the number (and thus, it wouldn't be prime).
        '''

        tot = 0

        # Non-nine digit is first to ninth from left:
        for pos in range(1,10):
            for i in [1,2,4,5,7,8]:
                num = i*10**(10-pos) + 9999999999 - 9*10**(10-pos)
                if isprime(num):
                    tot += num

        # Non-three digit is last one:
        for i in [1,7]:
            num = i + 9999999990
            if isprime(num):
                tot += num

        return tot

    TSNd  = d0() + d1() + d2() + d3() + d4() 
    TSNd += d5() + d6() + d7() + d8() + d9()

    print(TSNd)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1,2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 310 s (pypy)
# f1: ~ 102 ms (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
