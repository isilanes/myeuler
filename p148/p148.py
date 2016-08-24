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

def f3(nlines):

    print("--- f3 ---")

    ndiv = 1 # first line
    line = np.zeros(nlines, dtype=np.int)
    line[0] = 1
    for i in range(2,nlines+1):
        line[1:i] = (line[1:i] + line[:i-1]) % 7
        ndiv += np.count_nonzero(line)

    print(ndiv)

    return ndiv

def f4(nlines):

    print("--- f4 ---")

    ndiv = 1
    old_line = [1]
    for i in range(2,nlines+1):
        line = np.zeros(i, dtype=np.int)
        line[:-1] = old_line
        line[1:] = (line[1:] + old_line) % 7
        line[-1] = 1
        ndiv += np.count_nonzero(line)
        old_line = line

    print(ndiv)

    return ndiv


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [4]:
        t = timeit.Timer('f{0}(10**5)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # pypy times

    # function  nlines  ------- time (ms) -------
    #                   python2  python3     pypy
    # f0:          100      1.1      1.2     24.7
    # f0:         1000     ~270    294.2    236.5
    # f0:         2000    ~1400   1305.0   1319.5

    # f1:         1000     ~270     ~251
    # f1:         2000    ~1510    ~1480 

    # f2:         1000     ~275     ~275
    # f2:         2000     ~995     ~910

    # f3:         1000      ~13      ~14 
    # f3:         2000      ~40      ~43 
    # f3:        10000     ~900     ~955 
    # f3:       100000   ~95000   ~98000 

    # f4:         1000               ~25 
    # f4:         2000               ~55 
    # f4:        10000              ~910 
    # f4:        50000            ~25000 
    # f4:       100000           ~101000

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
