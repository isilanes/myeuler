import timeit

def f0(nlines):

    print("--- f0 ---")

    ndiv = 1 # first line
    line = []
    for i in range(nlines-1):
        newline = [ a+b for a,b in zip(line, line[1:]) ]
        newline = [1] + newline + [1]
        line = newline
        ndiv += sum([ 1 for i in line if i % 7 ])

    print(ndiv)

    return ndiv

def f1(nlines):

    print("--- f1 ---")

    ndiv = 1 # first line
    line = []
    for i in range(nlines-1):
        newline = [ a+b for a,b in zip(line, line[1:]) ]
        newline = [1] + newline + [1]
        line = newline
        ndiv += sum([ 1 for i in line if i % 7 ])

    print(ndiv)

    return ndiv


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}(1000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# function  nlines  ------- time (ms) -------
#                   python2  python3     pypy
# f0:          100      1.1      1.2     24.7
# f0:         1000    229.9    206.4    236.5
# f0:         2000   1383.4   1305.0   1319.5

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.1f} ms'.format(i, times[i]*1000))
