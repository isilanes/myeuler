import timeit

#------------------------------------------------------------------------------#

def f0(M,N):
    print("--- f0 ---")

    # Horizontal rectangles of size m*n, within rectangle of size M*N
    for m in range(1,M+1):
        for n in range(1,N+1):
            c = (M - m + 1) * (N - n + 1)
            print m, "x", n, "=", c

    # Oblique rectangles are more complex. Take i = 0, 1, ..., 2*M as horizontal
    # indices evenly placed at every half-square, and j = 0, 1, ..., 2*N as their
    # vertical equivalent. Every vertex of an oblique rectangle will lie in some
    # (i,j) point. We will check each valid top left vertex, and see how many
    # rectangles it can form by varying the W width and H height of the potential
    # rectangle, and seeing if the resulting top right, bottom-left and bottom-right
    # vertices are within the MxN figure (that is, the (i,j) of all vertices are
    # within (0,0) and (imax, jmax), i.e. (2*M, 2*N).
    for i in range(2*M):
        for j in range()


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(3,2)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxn   t (ms) - v = 1.0

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
