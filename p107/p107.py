#--------------------------------------------------------------------#

def f0(N):
    print("--- f0 ---")

    import numpy as np

    # Grid with all network info:
    G = np.zeros((40,40), dtype=np.int)

    # Read grid info:
    with open("network.txt") as f:
        iline = 0
        for line in f:
            aline = []
            a = line.strip().split(',')
            for e in a:
                if e == '-':
                    aline.append(0)
                else:
                    aline.append(int(e))
            G[iline,:] = aline[:]
            iline += 1

    s0 = sum(sum(G))

    # Keep looping over check on upper right cells until complete
    # cycle without removal. A cell is removed IFF its value is max
    # in its column AND max in its row AND removing it doesn't leave
    # the column NOR row empty.
    removal = True
    while removal:
        removal = False
        for icol in range(1,40):
            for irow in range(40):
                # Max and second max in row:
                max1, max = sorted(G[irow,:])[-2:]
                if G[irow,icol] == max and max1 > 0:
                    # Then check column:
                    max1, max = sorted(G[:,icol])[-2:]
                    if G[irow,icol] == max and max1 > 0:
                        G[irow,icol] = 0
                        G[icol,irow] = 0
                        removal = True

    s1 = sum(sum(G))

    print (s0 - s1) / 2

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}(7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
