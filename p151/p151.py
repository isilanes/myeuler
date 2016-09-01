# -*- coding=utf-8 -*-

import sys
import random
sys.path.append("..")

from libeuler import core

class p151(core.FunctionSet):

    def f0(self, n):
        """Naïve solution, using a simulation. Requires millions, possibly billions
        of rounds to get a result accurate enough."""

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


        n = int(self.opt.nvals)

        tot = 0
        for i in range(n): # run simulation n times
            single = -1 # the last one will be one
            E = Envelope([Sheet(2), Sheet(3), Sheet(4), Sheet(5)])
            while E.sheets:
                if len(E.sheets) == 1:
                    single += 1
                E.extract()
            tot += single

        return float(tot)/n

    def f1(self, n):
        """Very fast and simple solution."""

        debug = False

        class Envelope(object):

            def __init__(self, sheets):
                self.sheets = sheets

            def extract(self, i):
                """Extract i-th sheet from Envelope.
                Return resulting Envelope."""

                s = self.sheets[i]
                sheets = self.sheets[:i] + self.sheets[i+1:]
                sheets.extend(s.cut())

                return Envelope(sheets)

            def extract_all(self):
                """Perform all possible extractions from Envelope, and return all outcomes,
                in the form of a list of resulting Envelopes."""

                ret = []
                for i in range(len(self.sheets)):
                    ret.append(self.extract(i))

                return ret

            def __str__(self):
                return "-".join(sorted([str(x) for x in self.sheets]))

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


        if debug:
            space = ""

        tot = 0
        S = [ (1.0, Envelope([Sheet(2), Sheet(3), Sheet(4), Sheet(5)])) ]
        for i in range(14):
            ensemble = {}
            for frac,E in S:
                if len(E.sheets) == 1:
                    tot += frac

                if debug:
                    string = "{sp}{f:9.6f}: {e}".format(sp=space, f=frac, e=E)
                    print(string)

                ret = E.extract_all()
                frac2 = frac/len(E.sheets)
                for E2 in ret:
                    k = str(E2)
                    new = frac2
                    if k in ensemble:
                        new += ensemble[k][0]
                    ensemble[k] = (new, E2)

            S = [ x for x in ensemble.values() ]
            if debug:
                space += "  "

        return "{t:.6f}".format(t=tot)


P = p151(df="1", dn="0")
P.run()

# Python 3.5.2 times (Skinner)
#
#    n      res(n)  function  time (ms)
#
#    -    0.464399        f1        4.5

