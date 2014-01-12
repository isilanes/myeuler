#--------------------------------------------------------------------#

def f0(N=10):
    print("--- f0 ---")

    import math

    # Recall, we are looking for:
    #
    # (B/N)*(B-1)/(N-1) = 1/2

    while True:
        R = math.sqrt(1 + 2*N*(N-1))
        B = (1 + R)/2 # the -R solution would be < 0, and thus invalid
        B = int(B)

        if 2*B*(B-1) == N*(N-1):
            print(B)
            break

        N += 1

#--------------------------------------------------------------------#

def f1(Nmin=10):
    print("--- f1 ---")

    import math

    # Recall, we are looking for:
    #
    # (B/N)*(B-1)/(N-1) = 1/2
    #
    # Then:
    #
    # B = (1 + sqrt(1+2N*(N-1))))/2, the - part is not valid
    #
    # so we need:
    #
    # 1 + 2N(N-1) = k**2, where k == odd integer
    #
    # and: N = (1 + sqrt(2*k**2-1))/2

    k = 1 + 2*Nmin*(Nmin -1)
    k = math.sqrt(k)
    k = int(k)
    if not k % 2:
        k += 1

    while True:
        s = 2*k**2 - 1
        r = math.sqrt(s)
        r = int(r)
        if r*r == s:
            N = (1 + math.sqrt(2*k**2 - 1)) / 2
            N = int(N)
            r = math.sqrt(1 + 2*N*(N-1))
            B = (1 + r)/2 # the -R solution would be < 0, and thus invalid
            B = int(B)
            print(B)
            break
        k += 2

#--------------------------------------------------------------------#

def f2(Nmin=10):
    print("--- f2 ---")

    import math

    # Recall, we are looking for:
    #
    # (B/N)*(B-1)/(N-1) = 1/2
    #
    # Then:
    #
    # B = (1 + sqrt(1+2N*(N-1))) / 2, the - part is not valid
    #
    # and:
    #
    # N = (1 + sqrt(1+8B*(B-1))) / 2, the - part is not valid

    def fB(N):
        '''
        Given an N, return integer part of B.
        '''

        B = (1 + math.sqrt(1 +2*N*(N-1))) / 2
        return int(B)

    def fN(B):
        '''
        Given B, return integer part of N.
        '''

        N = (1 + math.sqrt(1 +8*B*(B-1))) / 2
        return int(N)

    N = Nmin
    while True:
        B = fB(N)
        if 2*B*(B-1) == N*(N-1):
            print(B)
            break
        B += 2
        N = fN(B)
        if 2*B*(B-1) == N*(N-1):
            print(B)
            break
        N += 2

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(3):
    t = timeit.Timer('f{0}(10**6)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: too slow (~ 1400 s for 10**9 with pypy)
# f1: too slow (~ 5400 s for 10**9 with pypy)
# f2: too slow (~  895 s for 10**9 with pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
