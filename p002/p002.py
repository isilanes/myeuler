# -*- coding=utf-8 -*-

import timeit
import inspect
import argparse

def parse_args():
    """Read and parse arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--functions",
            help="Comma-separated list of integers i,j..., to run functions fi, fj... Default: 0.",
            default="0")

    parser.add_argument("-n", "--nvals",
            help="Comma-separated list of integers n,m..., to run functions fi(n), fi(m)... Default: 4000000.",
            default="4000000")


    return parser.parse_args()

def f0(n, disp=True):

    if disp:
        print("--- {f}({n}) ---".format(f=inspect.stack()[0][3], n=n)) # print function name

    last1, last2 = 1, 2
    sum = 2
    while True:
        new = last1 + last2

        if new > n:
            break

        if not new % 2: # even
            sum += new

        last1, last2 = last2, new

    if disp:
        print(sum)

    return sum


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    # Parse command-line arguments:
    o = parse_args()

    # List of functions:
    fis = []
    if o.functions:
        fis = [int(i) for i in o.functions.split(",")]

    # List of N values:
    ns = []
    if o.nvals:
        ns = [int(i) for i in o.nvals.split(",")]

    # Execute all functions with all N values:
    times = []
    for i in fis:
        for n in ns:
            t = timeit.Timer('f{i}({n})'.format(i=i, n=n), "from __main__ import f{0}".format(i))
            times.append([[i,n], t.timeit(number=1)])

    # Print out times:
    print("\nTimes:\n")
    for (i,n),t in times:
        if t < 2:
            print('f{i}({n}): {t:.1f} ms'.format(i=i, t=t*1000, n=n))
        else:
            print('f{i}({n}): {t:.1f} s'.format(i=i, t=t, n=n))

    # Python 3.5.2 times (Skinner)
    #
    #        n      res(n)  function  time (ms)
    #
    #  4000000     4613732       f0        2.1

