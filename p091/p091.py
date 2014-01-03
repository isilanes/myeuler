#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def dot(v,w):
        '''
        Returns dot product of vectors v and w. If zero, v and w
        are orthogonal.
        '''

        return v[0]*w[0] + v[1]*w[1]

    def subt(v,w):
        '''
        Return the vector resulting from subtracting v - w.
        '''

        return (v[0] - w[0], v[1] - w[1])

    def isright(p,q):
        '''
        Return True if (0,0)--p--q is a right triangle, False otherwise.
        '''

        # Corner in (0,0):
        if not dot(p,q):
            return True

        # Corner in p:
        pq = subt(q,p)
        if not dot(p, pq):
            return True

        # Corner in q:
        qp = subt(p,q)
        if not dot(q,qp):
            return True

        return False

    # Loop over all possibilities:
    N = 50
    res = 0
    points = [ (x,y) for x in range(N+1) for y in range(N+1) if not (x,y) == (0,0) ]
    for v,w in it.combinations(points,2):
        if isright(v,w):
            res += 1

    print(res)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~0.3 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
