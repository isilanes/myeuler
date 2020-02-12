"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math

from libeuler import core


class CurrentSet(core.FunctionSet):

    def f0(self, n):
        factors = []
        
        num = n
        max = num
        cum = 1
        
        last = 2
        while num > last:
            for i in range(last,max):
                while not num % i:
                    factors.append(i)
                    num = num/i
                    cum = cum*i
                    last = i
                if cum == n:
                    break

        return factors[-1]

    def f1(self, n):

        def smallest(num, start):
            """Returns smallest (thus, prime) subfactor of "num" that is
            larger than "start"."""

            for i in range(start,int(math.sqrt(num)+1),2):
                if not num % i: # divisible
                    return i

            # If we reach thus far, there is no subfactor: number itself is prime:
            return num


        res = 1

        # First, take out twos:
        num = n
        while not num % 2: # while even
            num = num // 2
            res = 2

        # Then from 3 on:
        fac = 3
        while num > 1:
            fac = smallest(num, fac)
            num = num // fac
            res = fac

        return res

    def f2(self, n):

        mf = 0

        # First, take out twos:
        num = n
        while not num % 2: # while even
            num = num // 2
            mf = 2

        # Then from 3 on:
        for fac in range(3, n, 2):
            while not num % fac:
                num = num // fac
                mf = fac

            if num == 1:
                break

        return mf


P = CurrentSet()
P.run()
