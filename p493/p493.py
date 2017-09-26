"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij)
"""

# Standard libs:
import sys
import random
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p493(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n=1000):
        """Rubbish."""

        def ncolors(urn):
            n = 0
            for letter in ["A", "B", "C", "D", "E", "F", "G"]:
                if letter in urn:
                    n += 1

            return n


        # Set up:
        URN = ["A", "B", "C", "D", "E", "F", "G"]*10

        tot = 0.0001
        old_ave = 0
        min_diff = 10
        for i in range(1, n):
            sample = random.sample(URN, 20)
            n = ncolors(sample)
            tot += n
            ave = tot/i
            diff = abs(ave - old_ave)
            if diff * 10 < min_diff:
                string = "{i:8d} {n:2d} {a:13.10f} {d:13.10f}".format(i=i, n=n, a=ave, d=diff)
                print(string)
                min_diff = diff

            old_ave = ave
            if diff < 10**-9:
                return "{a:.9f}".format(a=ave)

        return ave, diff

    def f1(self, n=None):
        # Probability to pick 6 colors:
        # p6 = c1 * p(not A)
        # where:
        # c1 = amount of combinations of 1 color (7)
        # p(not A) = probability of not picking color A
        p6 = 7
        for i in range(20):
            p6 *= (60-i)/(70-i)

        # Probability to pick 5 colors:
        # p5 = c2 * p(not A, not B)
        # c2 = 6+5+4+3+2+1 = 21
        p5 = 21
        for i in range(20):
            p5 *= (50-i)/(70-i)

        # Probability to pick 4 colors:
        # p4 = c3 * p(not A, not B, not C)
        # c3 = 35
        p4 = 35
        for i in range(20):
            p4 *= (40-i)/(70-i)

        # Probability to pick 3 colors:
        # p3 = c4 * p(not A, not B, not C, not D)
        # c3 = c4 = 35
        p3 = 35
        for i in range(20):
            p3 *= (30-i)/(70-i)

        # Probability to pick 2 colors:
        # p2 = c5 * p(not A, not B, not C, not D, not E)
        # c5 = c2 = 21
        p2 = 21
        for i in range(20):
            p2 *= (20-i)/(70-i)

        # Probability to pick 7 colors:
        p7 = 1 - p6 - p5 - p4 - p3 - p2

        # Expected value:
        expected = 7*p7 + 6*p6 + 5*p5 + 4*p4 + 3*p3 + 2*p2

        return "{e:.9f}".format(e=expected)



# Main code:
if __name__ == "__main__":
    P = p493()
    P.run()

# Benchmarks:
benchmarks = {
    "Python 3.6.2 (Burns)": {
        "f0": {
            "skip": False,
            "data": [ # n, result, time (ms)
                [ 2,                0,     0.01 ],
            ],
        },
    },
}
