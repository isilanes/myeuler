# Standard libs:
import sys
import argparse
from datetime import datetime

# Constants:
DEFAULT_F = "0" # which function to run, default first (zero)
DEFAULT_N = "1" # what argument to pass to function(s), default 1

# Functions:
def parse_args(args=sys.argv[1:]):
    """Read and parse arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--functions",
            help="Comma-separated list of integers i, j..., to run functions fi,\
                    fj... Default: {d}.".format(d=DEFAULT_F),
            default=DEFAULT_F)

    parser.add_argument("-n", "--nvals",
            help="Comma-separated list of integers n, m..., to run functions fi(n),\
                    fi(m)... Default: {d}.".format(d=DEFAULT_N),
            default=DEFAULT_N)


    return parser.parse_args(args)


# Classes:
class FunctionSet(object):
    """Parent class for all solution sets."""

    # Constructor:
    def __init__(self, disp=True):
        self.disp = disp


    # Public methods:
    def f0(self, n):
        """f(i) should be the solutions proposed."""

        raise NotImplementedError

    def run(self):
        """Perform a run of all pertinent solutions."""

        # Parse command-line arguments:
        self.opts = parse_args()

        # List of functions:
        fis = []
        if self.opts.functions:
            fis = [int(i) for i in self.opts.functions.split(",")]

        # List of N values:
        ns = []
        if self.opts.nvals:
            ns = [int(i) for i in self.opts.nvals.split(",")]

        # Execute all functions with all N values:
        times = []
        for i in fis:
            for n in ns:
                now = datetime.now()

                if self.disp:
                    print("--- f{i}({n}) ---".format(i=i, n=n)) # print function name

                fun = getattr(self, "f{}".format(i))
                ret = fun(n)

                if self.disp:
                    print(ret)

                dt = (datetime.now() - now).total_seconds()
                times.append([[i,n], dt])

        # Print out times:
        print("\nTimes:\n")
        for (i,n),t in times:
            if t < 2:
                print('f{i}({n}): {t:.1f} ms'.format(i=i, t=t*1000, n=n))
            else:
                print('f{i}({n}): {t:.1f} s'.format(i=i, t=t, n=n))

