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
                print n, '->', k
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
                print "n=", n, 'A(n)=', k
                return
        n += 2


#------------------------------------------------------------------------------#

import timeit

times = []
for i in [1]:
    t = timeit.Timer('f{0}(10)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:   45s for A(n) > 1000
# f1: 260ms for A(n) > 1000
# f1:   48s for A(n) > 5000
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
