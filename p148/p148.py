import timeit
import numpy as np

def f0(nlines):

    print("--- f0 ---")

    ndiv = 1 # first line
    line = []
    for i in range(nlines-1):
        newline = [ a+b for a,b in zip(line, line[1:]) ]
        newline = [1] + newline + [1]
        line = newline
        ndiv += sum([ 1 for k in line if k % 7 ])

    print(ndiv)

    return ndiv

def f1(nlines):

    print("--- f1 ---")

    ndiv = 1 # first line
    line = [ 0 for i in range(nlines) ]
    line[0] = 1
    for i in range(2,nlines+1):
        line[i-1] = 1
        for j in range(i-2,0,-1):
            line[j] += line[j-1]
        ndiv += sum([ 1 for k in line if k % 7 ])

    print(ndiv)

    return ndiv

def f2(nlines):

    print("--- f2 ---")

    ndiv = 1 # first line
    line = np.zeros(nlines, dtype=np.int)
    line[0] = 1
    for i in range(2,nlines+1):
        line[i-1] = 1
        for j in range(i-2,0,-1):
            line[j] = (line[j] + line[j-1]) % 7
        ndiv += np.count_nonzero(line)

    print(ndiv)

    return ndiv


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [0,1,2]:
        t = timeit.Timer('f{0}(1*10**4)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # pypy times

    # function  nlines  ------- time (ms) -------
    #                   python2  python3     pypy
    # f0:          100      1.1      1.2     24.7
    # f0:         1000    229.9    206.4    236.5
    # f0:         2000   1383.4   1305.0   1319.5

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
