# -*- coding=utf-8 -*-

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?"""

import sys
import math
import random
sys.path.append("..")

from libeuler import core

class problem(core.FunctionSet):

    def f0(self, nth):
        primes = [2,3]
        i = primes[-1] + 2
        while len(primes) < nth:
            is_prime = True
            for prime in primes:
                if prime * prime > i:
                    break
                if not i % prime:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)

            i += 2

        return primes[-1]

    def f1(self, num):
        """Bordonau's answer."""

        def es_primo(numero):
            primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
            return primo


        it = 3
        position = 2
        while position < num:
            it +=2
            if es_primo(it):
                position +=1
        return it

    def f2(self, num):
        """Bordonau's answer, bugfixed."""

        def es_primo(numero):
            if not numero % 2:
                return False

            for i in range(3, int(math.sqrt(numero))+1, 2):
                if not numero % i:
                    return False
            return True


        it = 3
        position = 2
        while position < num:
            it +=2
            if es_primo(it):
                position += 1
        return it


P = problem(df="0", dn="10001")
P.run()
