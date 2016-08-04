import timeit

def f0(M,N):
    print("--- f0 ---")

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
