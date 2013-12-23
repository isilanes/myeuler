#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    Lmax = 2000

    n1 = 0
    for L in range(12,Lmax+1):
        already = False
        salir = False
        for A in range(3,L/3):
            for B in range(A,(L-A)/2+1):
                C = L - A - B
                if A**2 + B**2 == C**2:
                    if already: # then this is second case, so ignore
                        salir = True
                        n1 += -1
                        break
                    else:
                        n1 += 1
                        already = True
            if salir:
                break

    print(n1)

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    Lmax = 2000

    tris = {}
    for A in range(3,Lmax/3+1):
        for B in range(A,Lmax/2+1):
            for C in range(B+1,A+B):
                L = A + B + C
                if L > Lmax:
                    break
                if A**2 + B**2 == C**2:
                    if L in tris:
                        tris[L].append((A,B,C))
                    else:
                        tris[L] = [(A,B,C)]
                    break

    n1 = 0
    for v in tris.values():
        if len(v) == 1:
            n1 += 1

    print(n1)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): too slow. Struggles for even L=10k
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
