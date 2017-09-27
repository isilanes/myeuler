"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij)
"""

# Standard libs:
import sys
import random
sys.path.append(".")
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p493(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n=1000):
        """Brute force. Makes little sense, but serves to make checks."""

        # Constants:
        COLORS = ["A", "B", "C", "D", "E", "F", "G"]
        URN = COLORS*10

        def ncolors(pick):
            n = 0
            for color in COLORS:
                if color in pick:
                    n += 1

            return n


        # Set up:
        frequencies = {}

        tot = 0.0
        old_ave = 0
        for i in range(1, n+1):
            sample = random.sample(URN, 20)
            nc = ncolors(sample)
            frequencies[nc] = frequencies.get(nc, 0) + 1
            tot += nc
            ave = tot/i
            old_ave = ave

        for i in range(2, 8):
            freq = frequencies.get(i, 0) / n
            print(i, freq)

        return ave, frequencies

    def f1(self, n=None):
        """[WRONG] Makes no sense why it doesn't work. Maybe precision thing."""

        # Probability to pick 6 colors OR LESS:
        # p6less = c1 * p(not A)
        # where:
        # c1 = amount of combinations of 1 color (7)
        # p(not A) = probability of not picking color A
        p6less = 7
        for i in range(20):
            p6less *= (60.-i)/(70-i)

        # Probability to pick 5 colors OR LESS:
        # p5less = c2 * p(not A, not B)
        # c2 = 6+5+4+3+2+1 = 21
        p5less = 21
        for i in range(20):
            p5less *= (50.-i)/(70-i)

        # Probability to pick 4 colors OR LESS:
        # p4less = c3 * p(not A, not B, not C)
        # c3 = 35
        p4less = 35
        for i in range(20):
            p4less *= (40.-i)/(70-i)

        # Probability to pick 3 colors OR LESS:
        # p3less = c4 * p(not A, not B, not C, not D)
        # c4 = c3 = 35
        p3less = 35
        for i in range(20):
            p3less *= (30.-i)/(70-i)

        # Probability to pick 2 colors OR LESS:
        # p2less = c5 * p(not A, not B, not C, not D, not E)
        # c5 = c2 = 21
        p2less = 21
        for i in range(20):
            p2less *= (20.-i)/(70-i)

        # Probability to pick just 2 colors equal to 2 colors or less (p(less)=0):
        p2 = p2less

        # Probability to pick just N colors is N or less minus (N-1) or less:
        p3 = p3less - p2less
        p4 = p4less - p3less
        p5 = p5less - p4less
        p6 = p6less - p5less

        # Probability to pick 7 colors:
        p7 = 1 - p6less

        # Expected value:
        expected = 7*p7 + 6*p6 + 5*p5 + 4*p4 + 3*p3 + 2*p2

        return "{e:.9f}".format(e=expected)

    def f2(self, n=None):
        """[WRONG] Exactly as f1, but more accurate (lose less decimals).
        Preserving decimals above and beyond duty, exact same (wrong) result.
        """
        # Probability to pick 6 colors OR LESS:
        # p6less = c1 * p(not A)
        # where:
        # c1 = amount of combinations of 1 color (7)
        # p(not A) = probability of not picking color A
        num6less = 7
        div = 1
        for i in range(20):
            num6less *= (60.-i)
            div *= (70-i)

        # Probability to pick 5 colors OR LESS:
        # p5less = c2 * p(not A, not B)
        # c2 = 6+5+4+3+2+1 = 21
        num5less = 21
        for i in range(20):
            num5less *= (50.-i)

        # Probability to pick 4 colors OR LESS:
        # p4less = c3 * p(not A, not B, not C)
        # c3 = 35
        num4less = 35
        for i in range(20):
            num4less *= (40.-i)

        # Probability to pick 3 colors OR LESS:
        # p3less = c4 * p(not A, not B, not C, not D)
        # c3 = c4 = 35
        num3less = 35
        for i in range(20):
            num3less *= (30.-i)

        # Probability to pick 2 colors OR LESS:
        # p2less = c5 * p(not A, not B, not C, not D, not E)
        # c5 = c2 = 21
        num2less = 21
        for i in range(20):
            num2less *= (20.-i)

        # Probability to pick just 2 colors equal to 2 colors or less (p(less)=0):
        num2 = num2less

        # Probability to pick just N colors is N or less minus (N-1) or less:
        num3 = num3less - num2less
        num4 = num4less - num3less
        num5 = num5less - num4less
        num6 = num6less - num5less

        # Probability to pick 7 colors:
        num7 = div - num6less

        # Expected value:
        expected = (7*num7 + 6*num6 + 5*num5 + 4*num4 + 3*num3 + 2*num2) / div

        return "{e:.9f}".format(e=expected)

    def f3(self, n=None):
        """[WRONG] Assume each time we pick a ball, we drop it in the urn again before picking again."""

        # Probability to pick 6 colors OR LESS:
        # p6less = c1 * p(not A)
        # where:
        # c1 = amount of combinations of 1 color (7)
        # p(not A) = probability of not picking color A
        p6less = 7
        for i in range(20):
            p6less *= 60./70

        # Probability to pick 5 colors OR LESS:
        # p5less = c2 * p(not A, not B)
        # c2 = 6+5+4+3+2+1 = 21
        p5less = 21
        for i in range(20):
            p5less *= 50./70

        # Probability to pick 4 colors OR LESS:
        # p4less = c3 * p(not A, not B, not C)
        # c3 = 35
        p4less = 35
        for i in range(20):
            p4less *= 40./70

        # Probability to pick 3 colors OR LESS:
        # p3less = c4 * p(not A, not B, not C, not D)
        # c3 = c4 = 35
        p3less = 35
        for i in range(20):
            p3less *= 30./70

        # Probability to pick 2 colors OR LESS:
        # p2less = c5 * p(not A, not B, not C, not D, not E)
        # c5 = c2 = 21
        p2less = 21
        for i in range(20):
            p2less *= 20./70

        # Probability to pick 1 color:
        # p1 = c6 * p(not A, not B, not C, not D, not E, not F)
        # c6 = c1 = 7
        p1 = 7
        for i in range(20):
            p1 *= 10./70

        # Probability to pick just 2 colors equal to 2 colors or less minus 1 color:
        p2 = p2less - p1

        # Probability to pick just N colors is N or less minus (N-1) or less:
        p3 = p3less - p2less
        p4 = p4less - p3less
        p5 = p5less - p4less
        p6 = p6less - p5less

        # Probability to pick 7 colors:
        p7 = 1 - p6less

        # Expected value:
        expected = 7*p7 + 6*p6 + 5*p5 + 4*p4 + 3*p3 + 2*p2 + 1*p1

        return "{e:.9f}".format(e=expected)

    def f4(self, n=20):
        """Follow Jorge's idea, but reversed."""

        # Starting states:
        # states = {state: weight}
        # state is tuple with state[i] = c meaning 'c' colors have 'i' balls
        states = {
            tuple([0]*10 + [7]): 1.0,
        }

        # Produce all (unique) states after a succession of n extractions,
        # along with the weight of each one:
        balls = 70
        for ex in range(1, n+1):
            new_states = {}
            for state, weight in states.items():
                for i, amount in enumerate(state[1:]):
                    j = i + 1 # we are skipping state[0], remember
                    if amount:
                        new_amounts = list(state)
                        new_amounts[j] -= 1
                        new_amounts[j-1] += 1

                        new_state = tuple(new_amounts)
                        new_weight = weight * j*amount/balls

                        new_states[new_state] = new_states.get(new_state, 0) + new_weight

            states = new_states

            balls -= 1

        # Recap results:
        ave = 0
        for state, weight in states.items():
            ncolors = 7 - state[10]
            ave += ncolors * weight

        return "{a:.9f}".format(a=ave)


if __name__ == "__main__":
    P = p493()
    P.run()

# Benchmarks:
benchmarks = {
    "Python 3.5.2 (Skinner)": {
        "f1": {
            "skip": True,
            "data": [ # n, result, time (ms)
                [ 7, 6.812598295, 0.1 ],
            ],
        },
    },
}
