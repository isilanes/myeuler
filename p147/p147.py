import timeit

def f0(M,N):
    """This function is wrong."""

    print("--- f0 ---")
    return 0 # wrong function

    def NCA1(T, A, B, i, j):
        nca = 0
        r = max(0, B-i)
        Ap = A - r
        for k in range(Ap):
            for l in range(Ap-k):
                nca += (T - i - k) * (T - j - r - l)

        return nca

    def NCB1(T, A, B, i, j):
        ncb = 0
        r = max(0, A-i)
        q = max(0, B-j)
        Bp = B - r
        for k in range(Bp):
            for l in range(Bp-k):
                ncb += (T - i - q - k) * (T - j - r - l)

        return ncb

    def NEA1(T ,A):
        tot = 0
        for i in range(A):
            for j in range(A-i):
                tot += (T - i) * (T - j)

        print(["NEA1", tot])
        return tot

    def NEB1(T, A, B):
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
                tot -= NCA1(T, A, B, i, j)

        print(["NEA2", tot])
        return tot

    def NEB2(T,A,B):
        tot = 0
        for i in range(B):
            r = max(0, A-i)
            for j in range(B-i):
                q = max(0, B-j)
                tot += (T - i - q) * (T - j - r)
                tot -= NCB1(T, A, B, i, j)

        print(["NEB2", tot])
        return tot

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

        return NHR(T, T) - NEA1(T, A) - NEB1(T, A, B) - NEA2(T, A, B) - NEB2(T, A, B)


    # Horizontal rectangles, within rectangle of size M*N
    print(NHR(M, N))
    N = NHR(M, N) + NOR(M, N)

    print(N)

def f1(M,N, do_print=True):
    """First valid solution."""

    if do_print:
        print("--- f1 ---")

    def NHR(M,N):
        """Amount of horizontal rectangles of all sizes, within rectangle of size M*N."""
        
        tot = 0
        for i in range(1,M+1):
            for j in range(1,N+1):
                tot += (M - i + 1) * (N - j + 1)

        return tot

    def NOR(M,N):
        """Amount of oblique rectangles of all sizes, within rectangle of size M*N."""

        def jmin(A,i):
            return  max(0, A-i, i-A-1)

        def jmax(A,B,i):
            return min(A+B+1, A+1+i, A+2*B+2-i)
        
        def wmax(A,B,i,j):
            a = A + B + 2 -i
            b = A + 2 - i + j
            c = A + 2*B + 3 - i - j

            return min(a, b, c)

        def hmax(A,B,i,j,w):
            hm0 = jmax(A,B,i) - j + 1
            hm1 = jmax(A,B,i+w-1) - j + 1

            return min(hm0, hm1)

        
        A = M - 2
        B = N - 2
        T = A + B + 2

        tot = 0
        for i in range(T):
            for j in range(jmin(A,i), jmax(A,B,i)+1):
                for w in range(1,wmax(A,B,i,j)+1):
                    tot += hmax(A,B,i,j,w)

        return tot


    tot = 0
    for m in range(1,M+1):
        for n in range(1,N+1):
            tot += NHR(m, n) + NOR(m, n)
            
    if do_print:
        print(tot)

    return tot


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}(47,43)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times
# f0: 47x43  2030 ms

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
