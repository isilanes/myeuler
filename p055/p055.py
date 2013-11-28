#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    nlychrel = 0
    for number in range(10000):
        lychrel = True
        new = number
        for i in range(50):
            new = new + int(str(new)[::-1]) # reverse and add to itself
            if str(new) == str(new)[::-1]:  # whether it is a palindrome
                lychrel = False
                break

        if lychrel:
            nlychrel += 1

    print nlychrel

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 75 ms
