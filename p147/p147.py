import timeit

def f0(M,N):
    print("--- f0 ---")

<<<<<<< HEAD
    def NHR(M,N):
        """Amount of horizontal rectangles of all sizes, within rectangle of size M*N."""
        
        tot = 0
        for i in range(1,M+1):
            for j in range(1,N+1):
                tot += (M - i + 1) * (N - j + 1)

        return tot

    def NOR(M,N):
        """Amount of oblique rectangles of all sizes, within rectangle of size M*N."""
        
        T = M + N - 2
        A = M - 2
        B = N - 2

        return NHR(T,T) - NEA1(T,A) - NEB1(T,A,B) - NEA2(T,A,B) - NEB2(T,A,B)

    def NEA1(T,A):
        tot = 0
        for i in range(A):
            for j in range(A-i):
                tot += (T-i) * (T-j)

        print(["NEA1", tot])
        return tot

    def NEB1(T,A,B):
        tot = 0
        for i in range(B):
            r = max(0, A-i)
            for j in range(B-i):
                tot += (T - i) * (T - j - r)

        print(["NEB1", tot])
        return tot

    def NEA2(T,A,B):
        tot = 0
        for i in range(A):
            r = max(0, B-i)
            for j in range(A-i):
                tot += (T - i) * (T - j - r)

        NCA1 = 0
        tot -= NCA1

        print(["NEA2", tot])
        return tot

    def NEB2(T,A,B):
        tot = 0
        for i in range(A):
            r = max(0, A-i)
            for j in range(A-i):
                q = max(0, B-j)
                tot += (T -i - q) * (T - j - r)

        NCB1 = 0
        tot -= NCB1

        print(["NEB2", tot])
        return tot


    # Horizontal rectangles, within rectangle of size M*N
    print(NHR(M,N))
    N = NHR(M,N) + NOR(M,N)

    print(N)
=======

    class Rectangle(object):

        def __init__(self, M, N):
            self.M = M # horizonal size
            self.N = N # vertical size


    class Vertex(object):

        def __init__(self, i, j):
            self.i = i
            self.j = j

            # All (x,y) dimensions are doubled, i.e., a M*N rectangle is 
            # assumed to begin at x=0, y=0, and end at x=2M, y=2N.
            self.x = i + j
            self.y = 2 + i - j

        def is_within(self, R):
            '''Determine whether vertex is within the bounds of
            rectangle R.'''

            if self.x > 2*R.M:
                return False
            
            if self.y < 0 or self.y > 2*R.N:
                return False

            return True


    # Horizontal rectangles of size m*n, within rectangle of size M*N
    for m in range(1,M+1):
        for n in range(1,N+1):
            c = (M - m + 1) * (N - n + 1)
            print m, "x", n, "=", c
>>>>>>> 0ec45c58907f6fa0b22db306a037ee76d93193d9

    # Oblique rectangles are more complex. Take i = 0, 1, ..., 2*M as horizontal
    # indices evenly placed at every half-square, and j = 0, 1, ..., 2*N as their
    # vertical equivalent. Every vertex of an oblique rectangle will lie in some
    # (i,j) point. We will check each valid top left vertex, and see how many
    # rectangles it can form by varying the W width and H height of the potential
    # rectangle, and seeing if the resulting top right, bottom-left and bottom-right
    # vertices are within the MxN figure (that is, the (i,j) of all vertices are
    # within (0,0) and (imax, jmax), i.e. (2*M, 2*N).
    R = Rectangle(M, N)
    TL = Vertex(0,0)
    print TL.is_within(R)


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(3,2)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  MxN   t (ms) - v = 1.0

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
