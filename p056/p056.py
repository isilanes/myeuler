#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    maxdig = 1
    for a in range(1,100):
        for b in range(1,100):
            num = a**b
            digsum = sum( [ int(x) for x in str(num) ] )
            if digsum > maxdig:
                maxdig = digsum

    print maxdig

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 470 ms
