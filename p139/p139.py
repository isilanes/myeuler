import math
import timeit

#------------------------------------------------------------------------------#

def f0(max_perimeter):
    print("--- f0 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    npythagorean = 0
    for i in range(1,max_perimeter/3):
        i2 = i*i
        jmax = (i2-1)/2 + 1
        for j in range(i+1, jmax):
            if i + 2*j > max_perimeter:
                break
            k = issquare(i2+j*j)
            if k:
                if i + j + k > max_perimeter:
                    break
                sq = j - i
                if not k % sq:
                    npythagorean += 1
                    #print(i, j, k, sq)

    print(npythagorean)

def f1(max_perimeter):
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    npythagorean = 0
    k0 = 1
    while True:
        k0 += 1
        s = issquare(2*k0**2-1)
        i0 = (s - 1)/2
        if i0*3 >= max_perimeter:
            break
        if s:
            d = 0
            while True:
                d += 1
                i = i0*d
                j = (i0+1)*d
                k = k0*d
                if i+j+k >= max_perimeter:
                    break
                npythagorean += 1
                #print i, j, k, i+j+k

    print(npythagorean)


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}(10**4)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times:

# f0:  max_perimeter  t (ms)
#              10**3      32
#              10**4     124
#              10**5   10116

# f0:  max_perimeter  t (ms)
#              10**3       4
#              10**4       7
#              10**5      11
#              10**6      31
#              10**7     103
#              10**8    2411

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
