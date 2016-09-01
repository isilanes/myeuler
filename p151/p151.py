# -*- coding=utf-8 -*-

import timeit
import random
import inspect
import argparse
from datetime import datetime

def parse_args():
    """Read and parse arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--functions",
            help="Comma-separated list of integers i,j..., to run functions fi, fj... Default: None.",
            default=None)

    parser.add_argument("-n", "--nvals",
            help="Comma-separated list of integers n,m..., to run functions fi(n), fi(m)... Default: None.",
            default=None)


    return parser.parse_args()

def f0(n, disp=True):
    """Naïve solution, using a simulation. Requires millions, possibly billions
    of rounds to get a result accurate enough."""

    if disp:
        print("--- {f}({n}) ---".format(f=inspect.stack()[0][3], n=n)) # print function name

    class Envelope(object):

        def __init__(self, sheets):
            self.sheets = sheets

        def extract(self):
            """Extract one random sheet from envelope.
            Update self.sheets with resulting configuration."""

            i = random.randint(0,len(self.sheets)-1)
            s = self.sheets[i]
            self.sheets = self.sheets[:i] + self.sheets[i+1:]
            self.sheets.extend(s.cut())

            #print(s, "->", self)

        def __str__(self):
            return "-".join([str(x) for x in self.sheets])

    class Sheet(object):

        subs = {
            2: [3,4,5],
            3: [4,5],
            4: [5],
            5: [],
        }

        def __init__(self, size):
            self.size = size

        def cut(self):
            """Return list of Sheet objects resulting from cutting self."""

            return [Sheet(i) for i in self.subs[self.size]]

        def __str__(self):
            return "A{s.size}".format(s=self)


    tot = 0
    for i in range(n): # run simulation n times
        single = -1 # the last one will be one
        E = Envelope([Sheet(2), Sheet(3), Sheet(4), Sheet(5)])
        while E.sheets:
            if len(E.sheets) == 1:
                single += 1
            E.extract()
        tot += single
        frac = float(tot)/(i+1)
        #print("i=", i, "tot=", tot, "frac=", frac)

    ret = float(tot)/n
    if disp:
        print(ret)

    return ret


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    # Parse command-line arguments:
    o = parse_args()

    fis = []
    if o.functions:
        fis = [int(i) for i in o.functions.split(",")]

    ns = []
    if o.nvals:
        ns = [int(i) for i in o.nvals.split(",")]

    times = []
    for i in fis:
        for n in ns:
            t = timeit.Timer('f{i}({n})'.format(i=i, n=n), "from __main__ import f{0}".format(i))
            times.append([[i,n], t.timeit(number=1)])

    print("\nTimes:\n")
    for (i,n),t in times:
        if t < 2:
            print('f{i}({n}): {t:.1f} ms'.format(i=i, t=t*1000, n=n))
        else:
            print('f{i}({n}): {t:.1f} s'.format(i=i, t=t, n=n))

    # Python 3.4.3 times (Burns)
    #
    #    n     res(n)  function  time (ms)
    #
    #    2    -153582        f0        0.2
    #                        f1        0.1
