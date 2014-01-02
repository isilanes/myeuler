#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def intSF(L,W,H):
        '''
        Calculates shortest SF distance for L*W*H cuboid, which 
        happens to be:
        
        d**2 = (H+W)**2 + L**2

        and returns True if resulting d is integer, False otherwise.
        '''
        import math

        d2 = (H+W)**2 + L**2
        s = int(math.sqrt(d2))

        return s*s == d2

    min_ncubs = 1000*1000
    ncubs = 0
    A = 1
    while True:
        for B in range(1,A+1):
            for C in range(1,B+1):
                if intSF(A,B,C):
                    ncubs += 1

        if ncubs > min_ncubs:
            print(A, ncubs)
            break

        A += 1

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    def squares(N):
        '''
        Return all squares up to N**2, as a dictionary.
        '''
        res = {}
        for i in range(1,N):
            res[i*i] = True

        return res

    def intSF(L,W,H,sq):
        '''
        Calculates shortest SF distance for L*W*H cuboid, which 
        happens to be:
        
        d**2 = (H+W)**2 + L**2

        and returns True if resulting d is integer, False otherwise.
        Uses sq as a dictionary of squares, to avoid math.sqrt
        '''
        d2 = (H+W)**2 + L**2
        return d2 in sq
    
    MaxM = 6000
    sq = squares(MaxM)

    min_ncubs = 1000*1000
    ncubs = 0
    A = 1
    while True:
        for B in range(1,A+1):
            for C in range(1,B+1):
                if intSF(A,B,C, sq):
                    ncubs += 1

        if ncubs > min_ncubs:
            print(A, ncubs)
            break

        A += 1

        if 3*A > MaxM:
            print("Error, increase MaxM")
            break
    
#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 39 s
# f1: ~ 17 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
