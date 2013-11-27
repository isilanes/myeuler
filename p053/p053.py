#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")
    ngreater = 0
    for n in range(1,101):
        for r in range(1,n):
            if C(n,r) > 1000000:
                ngreater += 1

    print(ngreater)

#--------------------------------------------------------------------#

def C(n,r):
    A = min(r, n-r)
    B = max(r, n-r)
    Fn = 1
    for i in range(B+1, n+1):
        Fn = Fn*i

    FA = 1
    for i in range(1,A+1):
        FA = FA*i

    return Fn/FA

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 0.4 s
