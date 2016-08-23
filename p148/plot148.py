import pylab
import timeit
import argparse

from p148 import f0, f1, f2

def parse_args():
    """Read and parse arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--nums",
            help="Comma-separated list of N values, where N is the size of the problem. Default: None.",
            default=None)

    parser.add_argument("-f", "--funs",
            help="Comma-separated list of F values, where F is the F-th function to use and plot. Default: None.",
            default=None)


    return parser.parse_args()


# Parse command-line arguments:
o = parse_args()

if not o.nums or not o.funs:
    exit()

funs = sorted(o.funs.split(","))
nums = sorted([ int(x) for x in o.nums.split(",") ])

X, Y = {}, {}
for i in funs:
    X[i] = []
    Y[i] = []

    for n in nums:
        X[i].append(n)
        t = timeit.Timer('f{i}({n})'.format(i=i, n=n), "from __main__ import f{i}".format(i=i))
        t = t.timeit(number=1)
        Y[i].append(t)

pylab.figure(0)
for k in funs:
    label = "f{k}".format(k=k)
    pylab.plot(X[k], Y[k], 'o-', label=label)
pylab.xlim([0, int(nums[-1])])
pylab.legend()
pylab.show()
