#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import numpy as np

    def pn(coeffs,n):
        '''
        Return the value of polynomial with coefficients coeffs and
        x = n. E.g. coeffs = [1,2,3], n = 7:
        pn = 1 + 2*7 + 3*7**2 = 162
        '''

        res = 0
        for i in range(len(coeffs)):
            res += coeffs[i] * n**i
        
        return res

    # Build terms of exact polynomial:
    coeffs = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    nc = len(coeffs)
    un = [ pn(coeffs, n) for n in range(1,nc+1) ]

    # sum of FITs (sFIT) is un[0] (i.e. 1) for OP(1,n), as the first
    # term will be OP(1,n) = 1 = constant:
    sFIT = un[0]

    # Sum FITs for OP(2,n) to OP(10,n). Remember OP(N,n) is a N-1 
    # order polynomial.
    for N in range(2,nc):
        # Build a,b to solve with Python's linalg module:
        a = [ [n**i for i in range(N)] for n in range(1,N+1) ]
        b = un[:N]

        # X will hold the coefficients such that:
        # OP(N,n) = \sum_{i=0}^{N-1} X(i)*n**i
        X = np.linalg.solve(a,b)

        # Once we have X, use it to find FIT: 
        sFIT += pn(X,N+1)

    print(int(sFIT))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 83 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
