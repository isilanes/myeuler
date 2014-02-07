#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    Nmax = 200

    # dict k -> m(k)
    paths = [[1,2]]
    m = { 1: 0, 2: 1 }
    remaining = range(1,Nmax+1)
    remaining.remove(1)
    remaining.remove(2)

    # Begin branching:
    level = 2
    while remaining:
        newpaths = []
        for path in paths:
            for e in path:
                k = e + path[-1]
                if not k in m:
                    m[k] = level
                    if k in remaining:
                        remaining.remove(k)
                    newpath = path + [k]
                    newpaths.append(newpath)
                elif m[k] == level:
                    newpath = path + [k]
                    newpaths.append(newpath)
        paths = newpaths[:]
        level += 1

    tot = 0
    for i in range(1,Nmax+1):
        tot += m[i]
    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 140 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
