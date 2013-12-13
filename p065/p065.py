#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")
    
    nth = 100

    # Leading term of convergent:
    a0 = 2
    
    # Coefficients of convergent:
    coefs = [1, 2]
    for k in range(2, 35):
        coefs.extend([1, 1, 2*k])

    # Initialize loop and proceed:
    A, B = 1, coefs[nth-2]
    for i in range(nth-3,-1,-1):
        A, B = B, B*coefs[i] + A

    # The final numerator:
    numer = B*a0 + A

    # Sum of digits:
    print sum([ int(x) for x in str(numer) ])

#--------------------------------------------------------------------#

def f1():
    '''
    By Begoner @ https://projecteuler.net/thread=65
    '''
    print("--- f1 ---")
    m = 66
    n, d = m + 1, 1
    for i in xrange(m, 2, -2): n, d, m = n + d + (m - 2) * (d + n + n), d + n + n, m - 2
    print reduce(lambda x, y: int(x) + int(y), str(n * 3 + d * 2))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
