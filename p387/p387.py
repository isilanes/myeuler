"""
A Harshad or Niven number is a number that is divisible by the sum of its digits. 
201 is a Harshad number because it is divisible by 3 (the sum of its digits.) 
When we truncate the last digit from 201, we get 20, which is a Harshad number. 
When we truncate the last digit from 20, we get 2, which is also a Harshad number. 
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.

Also: 
    201/3=67 which is prime. 
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime. 
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable. 
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.
Find the sum of the strong, right truncatable Harshad primes less than 10**14.
"""

# Standard libs:
import sys
import math
import bisect
import itertools
from datetime import datetime
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p387(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n=10**8):

        # Generate length-n Harshads from lenght-n-1s:
        harshads = {
            1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        }
        for ndigits in range(2, 14):
            curr = []
            for pre_har in harshads[ndigits-1]:
                digit_sum_pre_har = sum([int(d) for d in str(pre_har)])
                for i in range(10):
                    har = pre_har * 10 + i
                    digit_sum = digit_sum_pre_har + i
                    if not har % digit_sum:
                        curr.append(har)
            harshads[ndigits] = curr

        # From all Harshads, pick strong ones:
        pass

        return


# Main code:
if __name__ == "__main__":
    P = p387()
    P.run()

# Benchmarks:
benchmarks = {
    "Python 3.6.2 times (Burns)": {
        "f0": {
            "skip": False,
            "data": [ # n, result, time (ms)
                [ 10**1,         3,      0.1 ],
            ],
        },
    },
}
