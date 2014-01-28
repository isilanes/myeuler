#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def find_prime(combo):
        '''
        Given string of digits "combo", find a prime by succesively
        concatenating first N digits for N=1,2,3... Return the
        first prime it finds, False if none found.
        '''

        num = ''
        for c in combo:
            num += str(c)
            if isprime(int(num)):
                return int(num)

        return False

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

    tot = 0
    #for combo in it.permutations([2,5,4,7,8,9,6,3,1], 9):
    for combo in it.permutations([1,2,3,4,5,6,7,8,9], 9):
        if combo[-1] in [0,2,4,5,6,8]:
            continue
        last = 0 # 
        while end < 9:
            primes = []
            while combo:
                res = find_prime(combo)
                if res:
                    primes.append(res)
                    i = len(str(res))
                    combo = combo[i:]
                    if not combo: # success! yay!
                        #print primes
                        tot += 1
                else:
                    break

    print(tot)

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
