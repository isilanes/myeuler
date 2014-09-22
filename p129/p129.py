import timeit

#------------------------------------------------------------------------------#

def f0(thres):
    print("--- f0 ---")

    def R(k):
        res = 0
        for i in range(k):
            res += 10**i
        return res


    success =  False

    n = 5
    i = 0
    while True:
        i += 1
        for j in range(4):
            n += 2
            k = 0
            while True:
                k += 1
                r = R(k)
                if not (r % n):
                    if k > thres:
                        success = True
                    break
            if success:
                print "n = {0} -> k = {1}".format(n, k)
                return
        n += 2

def f1(thres):
    print("--- f1 ---")

    def R(k):
        return int('1'*k)


    success =  False

    n = 5
    i = 0
    while True:
        i += 1
        for j in range(4):
            n += 2
            k = 0
            while True:
                k += 1
                r = R(k)
                if not (r % n):
                    if k > thres:
                        success = True
                    break
            if success:
                print "n = {0} -> k = {1}".format(n, k)
                return
        n += 2

def f2(thres):
    print("--- f2 ---")

    def remainder(n, k):
        '''Returns R(k) % n.'''

        rem = 0
        for i in range(k):
            rem = (rem + pow(10, i, n)) % n
        return rem


    for n in range(3,100000,2):
        if n % 5:
            for k in range(1,2000000):
                r = remainder(n, k)
                if not r:
                    break
            if k > thres:
                print "n = {0} -> k = {1}".format(n, k)
                break

def f3(thres):
    print("--- f3 ---")

    def A(n):
        '''Returns A(n) for n.'''

        k = 0
        rem = 0
        while True:
            rem = (rem + pow(10, k, n)) % n
            if not rem:
                return k + 1
            k += 1


    n = 17
    while True:
        if n % 5:
            a = A(n)
            if a > thres:
                print "n = {0} -> k = {1}".format(n, a)
                break
        n += 2

def f4(thres):
    print("--- f4 ---")

    def A(n):
        '''Returns A(n) for n.'''

        k = 1
        while True:
            rem = pow(10, k, n)
            if rem == 1:
                return k
            k += 1


    n = 17
    while True:
        if n % 5:
            a = A(n)
            if a > thres:
                print "n = {0} -> k = {1}".format(n, a)
                break
        n += 2


#------------------------------------------------------------------------------#

f4(5000)
exit()

times = []
for i in [3,4]:
    t = timeit.Timer('f{0}(1000*100)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:    A(n)   t (ms)
#        1000    45000

# f1:    A(n)   t (ms)
#        1000      260
#        5000    48000

# f2:    A(n)   t (ms)
#        1000     4750 :(

# f3:    A(n)   t (ms)
#        1000       56
#       10000     2890
#      100000   351500

# f4:    A(n)   t (ms)
#        1000       32
#       10000     2500
#      100000   260000

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
