#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")
    a = 3
    b = 2
    moredigs = 0
    for i in range(1000):
        if len(str(a)) > len(str(b)):
            moredigs +=1
        a, b = a + 2*b, a + b

    print (moredigs)

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 7 ms
