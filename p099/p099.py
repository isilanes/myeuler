#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math

    def largest(A,B):
        '''
        Returns A or B, whichever is largest. A and B are 
        both [a,b] pairs, meaning value == a**b.
        '''

        if A[1]*math.log(A[0]) - B[1]*math.log(B[0]) > 0:
            return A
        else:
            return B

    maxline = None
    max_be = [None, None]

    i = 0
    with open("base_exp.txt") as f:
        for line in f:
            i += 1
            B = [ int(x) for x in line.split(',') ]
            if not maxline:
                max_be = B
                maxline = i
            else:
                max_be = largest(max_be, B)
                if max_be == B:
                    maxline = i

    print(maxline)
    
#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    import math

    maxline = None
    maxlogb = 0

    i = 0
    with open("base_exp.txt") as f:
        for line in f:
            i += 1
            base, exp = [ int(x) for x in line.split(',') ]
            logb = exp*math.log(base)
            if logb > maxlogb:
                maxlogb = logb
                maxline = i

    print(maxline)
    
#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 3.3 ms (python)
# f1: ~ 2.2 ms (python)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
