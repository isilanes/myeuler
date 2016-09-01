# -*- coding=utf-8 -*-

import sys
sys.path.append("..")

from libeuler import core

class p002(core.FunctionSet):

    def f0(self, n):

        last1, last2 = 1, 2
        sum = 2
        while True:
            new = last1 + last2

            if new > n:
                break

            if not new % 2: # even
                sum += new

            last1, last2 = last2, new

        return sum


P = p002(df="0", dn="4000000")
P.run()
