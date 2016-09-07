# -*- coding=utf-8 -*-

import sys
import random
sys.path.append("..")

from libeuler import core

class problem(core.FunctionSet):

    def f0(self, num):
        factors = [2,3]
        for i in range(4,num+1):
            j = i
            for factor in factors:
                if not j % factor:
                    j = j // factor

            if j > 1:
                factors.append(j)

        res = 1
        for factor in factors:
            res = res * factor

        return res

    def f1(self, num):
        """Naïve version from Bordonau, verbatim."""

        i = 2
        while True:
            for divisor in range(2, num+1):
                isDivisor = True
                if i % divisor != 0:
                    isDivisor = False
                    break
            if isDivisor == True:
                return i

            i += 1


P = problem(df="0", dn="20")
P.run()
