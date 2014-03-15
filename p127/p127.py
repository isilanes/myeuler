#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def rad(N):
        '''
        Return rad(N), and the list of distinct primes that make up
        rad(N). E.g.:
        504 = 2**3 * 3**2 * 7 -> rad(504) = 2*3*7 = 42
        return 42, [2,3,7]
        '''

        r = 1
        facs = []
        for i in range(2,N+1):
            if not N % i:
                r = r * i
                facs.append(i)
                N = N / i
            while not N % i:
                N = N / i
            if N == 1:
                break
            i += 1
        
        return r, facs

    def invalid(i,facs):
        for fac in facs:
            if not i % fac:
                return True
        return False

    sumc = 0
    for c in range(1,5000):
        rad_c, facs_c = rad(c)
        rem_list = []
        for i in range(1,c):
            if not invalid(i, facs_c):
                rem_list.append(i)
            
        for j in range(len(rem_list)):
            a = rem_list[j]
            if 2*a > c:
                break
            rad_a, facs_a = rad(a)
            b = c - a
            if b in rem_list:
                if not invalid(b,facs_a):
                    rad_b, facs_b = rad(b)
                    rad_abc = rad_a * rad_b * rad_c
                    if rad_abc < c:
                        print a, b, c
                        sumc += c

    print(sumc)

#--------------------------------------------------------------------#

import timeit

times = []
for i in [0]:
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
