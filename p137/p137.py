import math
import timeit

#------------------------------------------------------------------------------#

def f0(nmax):
    print("--- f0 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        return k**2 == k2


    n = 1
    nnuggets = 0
    while True:
        k2 = 5*n**2 + 2*n + 1

        if issquare(k2):
            nnuggets += 1
            if nnuggets == nmax:
                print(n)
                break
        n += 1

def f1(nmax):
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    k = 2
    nnuggets = 0
    while True:
        rs = 5*k**2 - 4
        r = issquare(rs)
        if r:
            n5 = r-1
            if not n5 % 5:
                nnuggets += 1
        k += 1
        if nnuggets == nmax:
            print(n5/5)
            break

def f2(nmax):
    print("--- f2 ---")

    F1, F2 = 3, 2
    nnuggets = 0
    while True:
        F1, F2 = F1+F2, F1
        nnuggets += 1
        if nnuggets == nmax:
            print((int(math.sqrt(5*F1**2-4)) - 1)/5)
            break

        # skip 3:
        for i in range(3):
            F1, F2 = F1+F2, F1

def f3(nmax):
    '''Use Binet's formula to calculate nth Fibonacci number.'''

    print("--- f3 ---")

    phi = (1 + math.sqrt(5))/2
    n = 4*nmax + 1
    F = (phi**n - (-phi)**(-n))/math.sqrt(5)
    print((int(math.sqrt(5*F**2-4)) - 1)/5)


#------------------------------------------------------------------------------#

times = []
for i in [2,3]:
    t = timeit.Timer('f{0}(15)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  nmax  t (ms)
#         1       0.16
#         2       0.21
#         4       2.6
#         6       8.5
#         8      33
#        10    1186
#        11    7820
#        12     +++

# f1:  nmax  t (ms)
#         1       0.09
#         2       0.19
#         4       8
#         6       9
#         8      54
#        10    2546
#        11   17400

# f2 and f3: > 0.2 ms to solve for nmax=15

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
