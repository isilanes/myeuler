#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    class Sumas(object):


        def __init__(self):
            self.i = 2
            self.sums = [ [1, 1] ]

        def show(self):
            print(self.i)
            for suma in self.sums:
                print(suma)

        def grow(self):
            self.i += 1
            new = []
            for suma in self.sums:
                new.append(suma + [1])
                if suma[-1] < suma[-2]:
                    suma[-1] += 1
                    new.append(suma[:])

            new.append([self.i-1, 1])
            self.sums = new

    N = 50
    S = Sumas()
    for i in range(N-2):
        S.grow()
    #S.show()
    print(len(S.sums))

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    class Sumas(object):


        def __init__(self):
            self.i = 2
            self.oneone = 1 # how many sums end in [1, 1]
            self.sumsone = [] # sums that end in [x, 1], x > 1
            self.sums = [] # sums that do not end in [1]

        def show(self):
            print('\nN   = {0.i}'.format(self))
            print('N1  = {0}'.format(len(self.sumsone)))
            print('N11 = {0.oneone}'.format(self))
            print('Nx  = {0}'.format(len(self.sums)))

        def total(self):
            return len(self.sums) + self.oneone + len(self.sumsone)

        def grow(self):
            self.i += 1

            # Each x11 -> x11, plus each x1 -> x11
            self.oneone += len(self.sumsone)

            # Each x1 -> x (x2):
            newX = []
            for suma in self.sumsone:
                newX.append(suma[:-1]+[2])

            # Each x -> x1:
            self.sumsone = [ x + [1] for x in self.sums ]

            # Each x == xAB / A > B -> xAC / C = B+1:
            for suma in self.sums:
                if suma[-2] > suma[-1]:
                    suma[-1] += 1
                    newX.append(suma[:])
            self.sums = newX[:]

            # For self.i = N, add [N-1,1] to x1:
            self.sumsone.append([self.i-1, 1])

    N = 50
    S = Sumas()
    for i in range(N-2):
        S.grow()
    
    print(S.total())

#--------------------------------------------------------------------#

def f2():
    print("--- f2 ---")

    import numpy as np

    class Sumas(object):


        def __init__(self, N):
            self.i = 2
            # self.ends is a 2D array, where each element [A,B]
            # is an integer, showing how many combos end in A + B:
            self.ends = np.zeros((N,N), dtype=np.int)
            self.ends[1,1] = 1
            self.N = N

        def show(self):
            pass

        def total(self):
            return np.sum(self.ends, dtype=np.int)

        def grow(self):
            self.i += 1
            tmp = np.zeros((self.N,self.N), dtype=np.int)
            tmp[1,1] = self.ends[1,1]
            for A in range(2,N): # A = 1, then B = 1
                # B < A
                for B in range(1,A):
                    tmp[A,B+1] += self.ends[A,B]
                    tmp[B,1] += self.ends[A,B]

                # B = A
                tmp[A,1] += self.ends[A,A]

                # Always:
                tmp[self.i-1,1] = 1

            self.ends = tmp[:]

    N = 100
    S = Sumas(N)
    for i in range(N-2):
        S.grow()
    
    print(S.total())

#--------------------------------------------------------------------#

import timeit

# Values:
#  30      5603
#  40     37337
#  50    204225
#  60    966466
#  70   4087967
#  80  15796475
#  90  56634172
# 100 190569291

times = []
for i in range(3):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: scales badly (max N=70, t ~ 30s)
# f1: around 4.5x faster than f0, still scales badly
# f2: ~ 0.8 s. Scales linearly, so very nice.
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
