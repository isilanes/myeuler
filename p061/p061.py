#--------------------------------------------------------------------#

def f1(nmax):
    print("--- f1 ---")

    # All 4-digit triangulars:
    p3s = []
    i = 0
    while True:
        p = i*(i+1)/2
        if p > 9999:
            break
        elif p > 999:
            p3s.append(str(p))
        i += 1

    # All 4-digit squares:
    p4s = []
    i = 0
    while True:
        p = i*i
        if p > 9999:
            break
        elif p > 999:
            p4s.append(str(p))
        i += 1

    # All 4-digit pentagonals:
    p5s = []
    i = 0
    while True:
        p = i*(3*i-1)/2
        if p > 9999:
            break
        elif p > 999:
            p5s.append(str(p))
        i += 1

    # All 4-digit hexagonals:
    p6s = []
    i = 0
    while True:
        p = i*(2*i-1)
        if p > 9999:
            break
        elif p > 999:
            p6s.append(p)
        i += 1

    # All 4-digit heptagonal:
    p7s = []
    i = 0
    while True:
        p = i*(5*i-4)/2
        if p > 9999:
            break
        elif p > 999:
            p7s.append(p)
        i += 1

    # All 4-digit octagonal:
    p8s = []
    i = 0
    while True:
        p = i*(3*i-2)
        if p > 9999:
            break
        elif p > 999:
            p8s.append(p)
        i += 1

    # Find cycle:
    for p5 in p5s:
        A5, B5 = p5[:2], p5[3:]
        for p4 in p4s:
            A4, B4 = p4[:2], p4[3:]
            if A4 == B5:
                for p3 in p3s:
                    A3, B3 = p3[:2], p3[3:]
                    if A3 == B4 and B3 == A5:
                        print p5, p4, p3
                        return
            elif B4 == A5:
                for p3 in p3s:
                    A3, B3 = p3[:2], p3[3:]
                    if A3 == B4 and B3 == A5:
                        print p5, p4, p3
                        return

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1(1000)', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # doesn't work
