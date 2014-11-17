import timeit

#------------------------------------------------------------------------------#

def f0(maxd):
    print("--- f0 ---")

    def is_reversible(num):
        if not num % 10:
            return False

        revnum = int(str(num)[::-1])
        s = str(num+revnum)
        for d in s:
            if not int(d) % 2: # even
                return False
        return True


    nreversible = 0
    for i in range(10**maxd):
        if is_reversible(i):
            nreversible += 1

    print(nreversible)

def f1(maxd):
    print("--- f1 ---")

    nreversible = 0

    for dfirst in [ 1, 3, 5, 7, 9 ]:
        for dlast in [ 2, 4, 6, 8 ]:
            # Zero middle digits:
            if dfirst + dlast < 10:
                nreversible += 1

            # Middle n-2 digits:
            for i in range(10**(maxd-2)):
                carry = (dfirst + dlast) // 10
                mdigs = [ int(x) for x in str(i) ]
                reversible = True
                for d, rd in zip(mdigs, reversed(mdigs)):
                    s = d + rd + carry
                    if not s % 2:
                        reversible = False
                        break
                    carry = s // 10
                if reversible and not carry: # if carry, then it breaks the first+last = odd
                    nreversible += 1

    print(nreversible*2)

def f2(maxd):
    print("--- f2 ---")

    def is_reversible(num):
        if not num % 10:
            return False

        revnum = int(str(num)[::-1])
        s = str(num+revnum)
        for d in s:
            if not int(d) % 2: # even
                return False
        return True


    nreversible = 0
    for dfirst in [ 1, 3, 5, 7, 9 ]:
        for dlast in [ 2, 4, 6, 8 ]:
            # Zero middle digits:
            if dfirst + dlast < 10:
                nreversible += 1

            # n-2 middle digits:
            for nmid in range(1,maxd-1): # amount of middle digits
                for i in range(10**nmid):
                    num = dfirst*10**(nmid+1) + i*10 + dlast
                    if is_reversible(num):
                        nreversible += 1

    print(nreversible*2)


#------------------------------------------------------------------------------#

times = []
for i in [2]:
    t = timeit.Timer('f{0}(9)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0   nmax   t(ms)
#     10**3      14
#     10**6     654
#     10**7    7660
# too slow

# f1   wrong?

# f2   nmax   t(ms)
#     10**3       1.4
#     10**6     219
#     10**7    2100
#     10**8   20810
#     10**9  228770

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
