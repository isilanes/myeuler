import argparse
from datetime import datetime

class FunctionSet(object):

    def __init__(self, df, dn, disp=True):
        self.default_f = df
        self.default_n = dn
        self.disp = disp
        self.opt = None

    def parse_args(self):
        """Read and parse arguments"""

        parser = argparse.ArgumentParser()

        parser.add_argument("-f", "--functions",
                help="Comma-separated list of integers i,j..., to run functions fi, fj... Default: {d}.".format(d=self.default_f),
                default=self.default_f)

        parser.add_argument("-n", "--nvals",
                help="Comma-separated list of integers n,m..., to run functions fi(n), fi(m)... Default: {d}.".format(d=self.default_n),
                default=self.default_n)


        self.opt = parser.parse_args()

    def f0(self, n):

        return 0

    def run(self):
        # Parse command-line arguments:
        self.parse_args()

        # List of functions:
        fis = []
        if self.opt.functions:
            fis = [int(i) for i in self.opt.functions.split(",")]

        # List of N values:
        ns = []
        if self.opt.nvals:
            ns = [int(i) for i in self.opt.nvals.split(",")]

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
