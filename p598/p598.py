# Standard libs:
import sys
import math
import itertools
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p598(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n):
        """Basic, "by hand" result for C(10!).

        10! = 2**8 * 3**4 * 5**2 * 7
        if A * B = 10!, then:
        A = 2**a * 3**b * 5**c * 7**c
        B = 2**(8-a) * 3**(4-b) * 5**(2-c) * 7**(1-d)
         
        The amount of divisors would be:
        divA = (a+1) * (b+1) * (c+1) * (d+1)
        divB = (8-a+1) * (4-b+1) * (2-c+1) * (1-d+1)
         
        and we want to know when divA == divB
        """
        res = 0
        for a in range(9):
            for b in range(5):
                for c in range(3):
                    for d in range(2):
                        divA = (a+1)*(b+1)*(c+1)*(d+1)
                        divB = (9-a)*(5-b)*(3-c)*(2-d)
                        if divA == divB:
                            A = 2**a * 3**b * 5**c * 7**d
                            B = 2**(8-a) * 3**(4-b) * 5**(2-c) * 7**(1-d)
                            if A < B:
                                res += 1

        return res

    def f1(self, n):
        """Generalization of f0.
        Assumes argument "n" means C(n!).
        Too slow, it seems.
        """
        def combo2ndivs(combo, pvals):
            """Given a combo, return (divA, divB),
            meaning amount of divisors for combo and
            for complementary of combo (according to pvals).
            """
            divA, divB = 1, 1
            for i, c in enumerate(combo):
                divA *= c + 1
                divB *= pvals[i] - c + 1

            return divA, divB
        
        def combo2nums(combo, pkeys, pvals):
            """Return number given by combo exponents, and complementary."""
            A, B = 1, 1
            for i, c in enumerate(combo):
                A *= pkeys[i]**c
                B *= pkeys[i]**(pvals[i] - c)

            return A, B


        # Collect factors of n!:
        powers = {}
        for i in range(2, n+1):
            factors = core.factors_of(i)
            for factor in factors:
                powers[factor] = powers.get(factor, 0) + 1

        # Helper lists:
        pkeys = sorted(powers.keys())
        pvals = [powers[k] for k in pkeys]
        lists = [tuple(range(p+1)) for p in pvals]

        # Proceed:
        res = 0
        for combo in itertools.product(*lists):
            divA, divB = combo2ndivs(combo, pvals)
            if divA == divB:
                A, B = combo2nums(combo, pkeys, pvals)
                if A <= B:
                    #print(combo, A, B, divA, divB)
                    res += 1

        return res

    def f2(self, n=20):
        """Hand-crafted for n=20 (optimization test)."""

        TWO = 18
        THREE = 8
        FIVE = 4
        SEVEN = 2
        ELEVEN = 1
        THIRTEEN = 1
        SEVENTEEN = 1
        NINETEEN = 1

        res = 0
        for two in range(TWO+1):
            for three in range(THREE+1):
                for five in range(FIVE+1):
                    for seven in range(SEVEN+1):
                        for eleven in range(ELEVEN+1):
                            for thirteen in range(THIRTEEN+1):
                                for seventeen in range(SEVENTEEN+1):
                                    for nineteen in range(NINETEEN+1):
                                        divA = (two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1)*(thirteen+1)*(seventeen+1)*(nineteen+1)
                                        divB = (TWO+1-two)*(THREE+1-three)*(FIVE+1-five)*(SEVEN+1-seven)*(ELEVEN+1-eleven)*(THIRTEEN+1-thirteen)*(SEVENTEEN+1-seventeen)*(NINETEEN+1-nineteen)
                                        if divB < divA:
                                            break

                                        if divA == divB:
                                            A = 2**two * 3**three * 5**five * 7**seven * 11**eleven * 13**thirteen * 17**seventeen * 19**nineteen
                                            B = 2**(TWO-two) * 3**(THREE-three) * 5**(FIVE-five) * 7**(SEVEN-seven) * 11**(ELEVEN-eleven) * 13**(THIRTEEN-thirteen) * 17**(SEVENTEEN-seventeen) * 19**(NINETEEN-nineteen)
                                            if A < B:
                                                res += 1

        return res

    def f3(self, n=30):
        """Hand-crafted for n=30 (optimization test)."""

        TWO = 26
        THREE = 14
        FIVE = 7
        SEVEN = 4
        ELEVEN = 2
        THIRTEEN = 2
        SEVENTEEN = 1
        NINETEEN = 1
        TTHREE = 1
        TNINE = 1

        res = 0
        for two in range(TWO+1):
            for three in range(THREE+1):
                for five in range(FIVE+1):
                    for seven in range(SEVEN+1):
                        for eleven in range(ELEVEN+1):
                            for thirteen in range(THIRTEEN+1):
                                for seventeen in range(SEVENTEEN+1):
                                    for nineteen in range(NINETEEN+1):
                                        for tthree in range(TTHREE+1):
                                            for tnine in range(TNINE+1):
                                                divA = (two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1)*(thirteen+1)*(seventeen+1)*(nineteen+1)*(tthree+1)*(tnine+1)
                                                divB = (TWO+1-two)*(THREE+1-three)*(FIVE+1-five)*(SEVEN+1-seven)*(ELEVEN+1-eleven)*(THIRTEEN+1-thirteen)*(SEVENTEEN+1-seventeen)*(NINETEEN+1-nineteen)*(TTHREE+1-tthree)*(TNINE+1-tnine)
                                                if divB < divA:
                                                    break

                                                if divA == divB:
                                                    A = 2**two * 3**three * 5**five * 7**seven * 11**eleven * 13**thirteen * 17**seventeen * 19**nineteen * 23**tthree * 29**tnine
                                                    B = 2**(TWO-two) * 3**(THREE-three) * 5**(FIVE-five) * 7**(SEVEN-seven) * 11**(ELEVEN-eleven) * 13**(THIRTEEN-thirteen) * 17**(SEVENTEEN-seventeen) * 19**(NINETEEN-nineteen) * 23**(TTHREE-tthree) * 29**(TNINE-tnine)
                                                    if A < B:
                                                        res += 1

        return res

    def f4(self, n=30):
        """Better hand-crafted f3."""

        TWO = 26
        THREE = 14
        FIVE = 7
        SEVEN = 4
        ELEVEN = 2
        THIRTEEN = 2
        SEVENTEEN = 1
        NINETEEN = 1
        TTHREE = 1
        TNINE = 1

        K = (TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1)*(ELEVEN+1)*(THIRTEEN+1)*(SEVENTEEN+1)*(NINETEEN+1)*(TTHREE+1)*(TNINE+1)
        two = 26
        three = 10
        five = 6
        Kabc = (TWO-two+1)*(THREE-three+1)*(FIVE-five+1) / ((two+1)*(three+1)*(five+1))
        Rabc = Kabc / ((TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1))
        Cmax = int((Rabc*K*(SEVEN+1) - 1) / (1 + Rabc*K)) + 1

        res = 0
        count = 0
        for two in range(TWO+1):
            Ka = (TWO-two+1) / (two+1)
            Ra = Ka / ((TWO+1)*(THREE+1))
            three_max = (Ra*K*(THREE+1) - 1) // (1 + Ra*K) + 1
            three_max = int(three_max)
            for three in range(THREE+1):
                if three >= three_max:
                    break
                Kab = (TWO-two+1)*(THREE-three+1) / ((two+1)*(three+1))
                Rab = Kab / ((TWO+1)*(THREE+1)*(FIVE+1))
                five_max = (Rab*K*(FIVE+1) - 1) // (1 + Rab*K) + 1
                five_max = int(five_max)
                for five in range(FIVE+1):
                    if five >= five_max:
                        break
                    Kabc = (TWO-two+1)*(THREE-three+1)*(FIVE-five+1) / ((two+1)*(three+1)*(five+1))
                    Rabc = Kabc / ((TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1))
                    seven_max = (Rabc*K*(SEVEN+1) - 1) // (1 + Rabc*K) + 1
                    seven_max = int(seven_max)
                    for seven in range(SEVEN+1):
                        if seven >= seven_max:
                            break
                        Kabcd = (TWO-two+1)*(THREE-three+1)*(FIVE-five+1)*(SEVEN-seven+1) / ((two+1)*(three+1)*(five+1)*(seven+1))
                        Rabcd = Kabcd / ((TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1)*(ELEVEN+1))
                        eleven_max = (Rabcd*K*(ELEVEN+1) - 1) // (1 + Rabcd*K) + 1
                        eleven_max = int(eleven_max)
                        for eleven in range(ELEVEN+1):
                            if eleven >= eleven_max:
                                break
                            Kabcde = (TWO-two+1)*(THREE-three+1)*(FIVE-five+1)*(SEVEN-seven+1)*(ELEVEN-eleven+1) / ((two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1))
                            Rabcde = Kabcde / ((TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1)*(ELEVEN+1)*(THIRTEEN+1))
                            thirteen_max = (Rabcde*K*(THIRTEEN+1) - 1) // (1 + Rabcde*K) + 1
                            thirteen_max = int(thirteen_max)
                            for thirteen in range(THIRTEEN+1):
                                if thirteen >= thirteen_max:
                                    break
                                Kabcdef = (TWO-two+1)*(THREE-three+1)*(FIVE-five+1)*(SEVEN-seven+1)*(ELEVEN-eleven+1)*(THIRTEEN-thirteen+1) / ((two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1)*(thirteen+1))
                                Rabcdef = Kabcdef / ((TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1)*(ELEVEN+1)*(THIRTEEN+1)*(SEVENTEEN+1))
                                seventeen_max = (Rabcdef*K*(SEVENTEEN+1) - 1) // (1 + Rabcdef*K) + 1
                                seventeen_max = int(seventeen_max)
                                for seventeen in range(SEVENTEEN+1):
                                    if seventeen >= seventeen_max:
                                        break
                                    for nineteen in range(NINETEEN+1):
                                        for tthree in range(TTHREE+1):
                                            for tnine in range(TNINE+1):
                                                count += 1
                                                divA = (two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1)*(thirteen+1)*(seventeen+1)*(nineteen+1)*(tthree+1)*(tnine+1)
                                                divB = (TWO+1-two)*(THREE+1-three)*(FIVE+1-five)*(SEVEN+1-seven)*(ELEVEN+1-eleven)*(THIRTEEN+1-thirteen)*(SEVENTEEN+1-seventeen)*(NINETEEN+1-nineteen)*(TTHREE+1-tthree)*(TNINE+1-tnine)
                                                if divB < divA:
                                                    break

                                                if divA == divB:
                                                    A = 2**two * 3**three * 5**five * 7**seven * 11**eleven * 13**thirteen * 17**seventeen * 19**nineteen * 23**tthree * 29**tnine
                                                    B = 2**(TWO-two) * 3**(THREE-three) * 5**(FIVE-five) * 7**(SEVEN-seven) * 11**(ELEVEN-eleven) * 13**(THIRTEEN-thirteen) * 17**(SEVENTEEN-seventeen) * 19**(NINETEEN-nineteen) * 23**(TTHREE-tthree) * 29**(TNINE-tnine)
                                                    if A < B:
                                                        res += 1

        print(count)
        return res

    def f5(self, n):
        """Another approach.
        Much faster... yet not fast enough!
        It also uses a lot of memory.
        """
        # Initial factorization of n!:
        powers = {}
        for i in range(2, n+1):
            factors = core.factors_of(i)
            for factor in factors:
                powers[factor] = powers.get(factor, 0) + 1

        powers = [v for v in powers.values()]

        # Initialize with first:
        divisors = {}
        for i in range(powers[0]+1):
            f1 = i + 1
            f2 = powers[0] - i + 1
            k = (f1, f2)
            divisors[k] = 1

        # Populate with all the rest:
        for p in powers[1:]:
            new = {}
            for d, v in divisors.items():
                f1_pre, f2_pre = d
                for i in range(p+1):
                    f1 = f1_pre*(i + 1)
                    f2 = f2_pre*(p - i + 1)
                    k = (f1, f2)
                    new[k] = new.get(k, 0) + v

            divisors = new

        tot = 0
        for k, v in divisors.items():
            f1, f2 = k
            if f1 == f2:
                tot += v

        return tot // 2

    def f6(self, n):
        """Minor optimization of f5. Not good enough."""

        def ndiv(exp_list):
            """Return number of divisors from list of exponents."""

            n = 1
            for e in exp_list:
                n *= e + 1

            return n


        # Initial factorization of n!:
        powers = {}
        for i in range(2, n+1):
            factors = core.factors_of(i)
            for factor in factors:
                powers[factor] = powers.get(factor, 0) + 1

        powers = [v for v in powers.values()]
        ndivs = [ndiv(powers[i:]) for i in range(len(powers))]

        # Initialize with first:
        divisors = {}
        for i in range(powers[0]+1):
            f1 = i + 1
            f2 = powers[0] - i + 1
            ratio = max(f1, f2) / min(f1, f2)
            if ratio < ndivs[1]: # keep only the f1/f2 disparities "fixable" by remaining exponents
                k = (f1, f2)
                divisors[k] = 1

        # Populate with all the rest:
        for j, p in enumerate(powers[1:]):
            new = {}
            for d, v in divisors.items():
                f1_pre, f2_pre = d
                for i in range(p+1):
                    f1 = f1_pre*(i + 1)
                    f2 = f2_pre*(p - i + 1)
                    ratio = max(f1, f2) / min(f1, f2)
                    if ratio < ndivs[j+1]: # keep only the f1/f2 disparities "fixable" by remaining exponents
                        k = (f1, f2)
                        new[k] = new.get(k, 0) + v

            divisors = new

        # Extract the result (tot) we want:
        tot = 0
        for k, v in divisors.items():
            f1, f2 = k
            if f1 == f2:
                tot += v

        return tot // 2 # each result is duplicated

    def f7(self, n=30):
        """Optimization of f3 to account for n=A*B, A <= B, so A <= sqrt(n).
        Not much of an improvement, or at all.
        """
        TWO = 26
        THREE = 14
        FIVE = 7
        SEVEN = 4
        ELEVEN = 2
        THIRTEEN = 2
        SEVENTEEN = 1
        NINETEEN = 1
        TTHREE = 1
        TNINE = 1

        ncombos = (TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1)*(ELEVEN+1)*(THIRTEEN+1)*(SEVENTEEN+1)*(NINETEEN+1)*(TTHREE+1)*(TNINE+1)

        log2 = math.log(2)
        log3 = math.log(3)
        log5 = math.log(5)
        log7 = math.log(7)
        log11 = math.log(11)
        log13 = math.log(13)
        log17 = math.log(17)
        log19 = math.log(19)
        log23 = math.log(23)
        log29 = math.log(29)

        #LOGSQRT = (TWO/2.+1)*log2 + (THREE/2.+1)*log3 + (FIVE/2.+1)*log5 + (SEVEN/2.+1)*log7 + (ELEVEN/2.+1)*log11 + (THIRTEEN/2.+1)*log13 + (SEVENTEEN/2.+1)*log17 + (NINETEEN/2.+1)*log19 + (TTHREE/2.+1)*log23 + (TNINE/2.+1)*log29
        LOGSQRT = TWO/2.*log2 + THREE/2.*log3 + FIVE/2.*log5 + SEVEN/2.*log7 + ELEVEN/2.*log11 + THIRTEEN/2.*log13 + SEVENTEEN/2.*log17 + NINETEEN/2.*log19 + TTHREE/2.*log23 + TNINE/2.*log29

        res = 0
        hits = 0
        for two in range(TWO+1):
            lognum2 = two * log2
            if lognum2 > LOGSQRT:
                break
            for three in range(THREE+1):
                lognum3 = lognum2 + three * log3
                if lognum3 > LOGSQRT:
                    break
                for five in range(FIVE+1):
                    lognum5 = lognum3 + five * log5
                    if lognum5 > LOGSQRT:
                        break
                    for seven in range(SEVEN+1):
                        lognum7 = lognum5 + seven*log7
                        if lognum7 > LOGSQRT:
                            break
                        for eleven in range(ELEVEN+1):
                            lognum11 = lognum7 + eleven*log11
                            if lognum11 > LOGSQRT:
                                break
                            for thirteen in range(THIRTEEN+1):
                                lognum13 = lognum11 + thirteen*log13
                                if lognum13 > LOGSQRT:
                                    break
                                for seventeen in range(SEVENTEEN+1):
                                    lognum17 = lognum13 + seventeen*log17
                                    if lognum17 > LOGSQRT:
                                        break
                                    for nineteen in range(NINETEEN+1):
                                        lognum19 = lognum17 + nineteen*log19
                                        if lognum19 > LOGSQRT:
                                            break
                                        for tthree in range(TTHREE+1):
                                            lognum23 = lognum19 + tthree*log23
                                            if lognum23 > LOGSQRT:
                                                break
                                            for tnine in range(TNINE+1):
                                                lognum29 = lognum23 + tnine*log29
                                                if lognum29 > LOGSQRT:
                                                    break
                                                divA = (two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1)*(thirteen+1)*(seventeen+1)*(nineteen+1)*(tthree+1)*(tnine+1)
                                                divB = (TWO+1-two)*(THREE+1-three)*(FIVE+1-five)*(SEVEN+1-seven)*(ELEVEN+1-eleven)*(THIRTEEN+1-thirteen)*(SEVENTEEN+1-seventeen)*(NINETEEN+1-nineteen)*(TTHREE+1-tthree)*(TNINE+1-tnine)
                                                if divB < divA:
                                                    break

                                                hits += 1
                                                if divA == divB:
                                                    A = 2**two * 3**three * 5**five * 7**seven * 11**eleven * 13**thirteen * 17**seventeen * 19**nineteen * 23**tthree * 29**tnine
                                                    B = 2**(TWO-two) * 3**(THREE-three) * 5**(FIVE-five) * 7**(SEVEN-seven) * 11**(ELEVEN-eleven) * 13**(THIRTEEN-thirteen) * 17**(SEVENTEEN-seventeen) * 19**(NINETEEN-nineteen) * 23**(TTHREE-tthree) * 29**(TNINE-tnine)
                                                    if A < B:
                                                        res += 1


        print(hits, ncombos, hits/ncombos)

        return res

    def f8(self, n=30):
        """Tweak f7 further by inverting the order."""

        TWO = 26
        THREE = 14
        FIVE = 7
        SEVEN = 4
        ELEVEN = 2
        THIRTEEN = 2
        SEVENTEEN = 1
        NINETEEN = 1
        TTHREE = 1
        TNINE = 1

        ncombos = (TWO+1)*(THREE+1)*(FIVE+1)*(SEVEN+1)*(ELEVEN+1)*(THIRTEEN+1)*(SEVENTEEN+1)*(NINETEEN+1)*(TTHREE+1)*(TNINE+1)

        log2 = math.log(2)
        log3 = math.log(3)
        log5 = math.log(5)
        log7 = math.log(7)
        log11 = math.log(11)
        log13 = math.log(13)
        log17 = math.log(17)
        log19 = math.log(19)
        log23 = math.log(23)
        log29 = math.log(29)

        LOGSQRT = TWO/2.*log2 + THREE/2.*log3 + FIVE/2.*log5 + SEVEN/2.*log7 + ELEVEN/2.*log11 + THIRTEEN/2.*log13 + SEVENTEEN/2.*log17 + NINETEEN/2.*log19 + TTHREE/2.*log23 + TNINE/2.*log29

        res = 0
        hits = 0
        for tnine in range(TNINE+1):
            lognum29 = tnine * log29
            if lognum29 > LOGSQRT:
                break
            for tthree in range(TTHREE+1):
                lognum23 = lognum29 + tthree * log23
                if lognum23 > LOGSQRT:
                    break
                for nineteen in range(NINETEEN+1):
                    lognum19 = lognum23 + nineteen * log19
                    if lognum19 > LOGSQRT:
                        break
                    for seventeen in range(SEVENTEEN+1):
                        lognum17 = lognum19 + seventeen*log17
                        if lognum17 > LOGSQRT:
                            break
                        for thirteen in range(THIRTEEN+1):
                            lognum13 = lognum17 + thirteen*log13
                            if lognum13 > LOGSQRT:
                                break
                            for eleven in range(ELEVEN+1):
                                lognum11 = lognum13 + eleven*log11
                                if lognum11 > LOGSQRT:
                                    break
                                for seven in range(SEVEN+1):
                                    lognum7 = lognum11 + seven*log7
                                    if lognum7 > LOGSQRT:
                                        break
                                    for five in range(FIVE+1):
                                        lognum5 = lognum7 + five*log5
                                        if lognum5 > LOGSQRT:
                                            break
                                        for three in range(THREE+1):
                                            lognum3 = lognum7 + three*log3
                                            if lognum3 > LOGSQRT:
                                                break
                                            for two in range(TWO+1):
                                                lognum2 = lognum3 + two*log2
                                                if lognum2 > LOGSQRT:
                                                    break
                                                divA = (two+1)*(three+1)*(five+1)*(seven+1)*(eleven+1)*(thirteen+1)*(seventeen+1)*(nineteen+1)*(tthree+1)*(tnine+1)
                                                divB = (TWO+1-two)*(THREE+1-three)*(FIVE+1-five)*(SEVEN+1-seven)*(ELEVEN+1-eleven)*(THIRTEEN+1-thirteen)*(SEVENTEEN+1-seventeen)*(NINETEEN+1-nineteen)*(TTHREE+1-tthree)*(TNINE+1-tnine)
                                                if divB < divA:
                                                    break

                                                hits += 1
                                                if divA == divB:
                                                    A = 2**two * 3**three * 5**five * 7**seven * 11**eleven * 13**thirteen * 17**seventeen * 19**nineteen * 23**tthree * 29**tnine
                                                    B = 2**(TWO-two) * 3**(THREE-three) * 5**(FIVE-five) * 7**(SEVEN-seven) * 11**(ELEVEN-eleven) * 13**(THIRTEEN-thirteen) * 17**(SEVENTEEN-seventeen) * 19**(NINETEEN-nineteen) * 23**(TTHREE-tthree) * 29**(TNINE-tnine)
                                                    if A < B:
                                                        res += 1


        return res

    def f9(self, n=30):
        """(Crappy) generalization of f8.
        Yes, it's an optimization of method in f1.. but slower and scales worse than f5 and f6.
        """

        if n == 30:
            E2 = 26
            E3 = 14
            E5 = 7
            E7 = 4
            E11 = 2
            E13 = 2
            E17 = 1
            E19 = 1
            E23 = 1
            E29 = 1
            E31 = 0
            E37 = 0
        if n == 35:
            E2 = 32
            E3 = 15
            E5 = 8
            E7 = 5
            E11 = 3
            E13 = 2
            E17 = 2
            E19 = 1
            E23 = 1
            E29 = 1
            E31 = 1
            E37 = 0
        elif n == 40:
            E2 = 38
            E3 = 18
            E5 = 9
            E7 = 5
            E11 = 3
            E13 = 3
            E17 = 2
            E19 = 2
            E23 = 1
            E29 = 1
            E31 = 1
            E37 = 1
        else:
            # Collect factors of n!:
            powers = {}
            for i in range(2, n+1):
                factors = core.factors_of(i)
                for factor in factors:
                    powers[factor] = powers.get(factor, 0) + 1

            return powers

        ncombos = (E2+1)*(E3+1)*(E5+1)*(E7+1)*(E11+1)*(E13+1)*(E17+1)*(E19+1)*(E23+1)*(E29+1)*(E31+1)*(E37+1)

        log2 = math.log(2)
        log3 = math.log(3)
        log5 = math.log(5)
        log7 = math.log(7)
        log11 = math.log(11)
        log13 = math.log(13)
        log17 = math.log(17)
        log19 = math.log(19)
        log23 = math.log(23)
        log29 = math.log(29)
        log31 = math.log(31)
        log37 = math.log(37)

        LOGSQRT = E2/2.*log2 + E3/2.*log3 + E5/2.*log5 + E7/2.*log7 + E11/2.*log11 + E13/2.*log13 + E17/2.*log17 + E19/2.*log19 + E23/2.*log23 + E29/2.*log29 + E31*log31/2 + E37*log37/2

        res = 0
        hits = 0
        for e37 in range(E37+1):
            lognum37 = e37 * log37
            if lognum37 > LOGSQRT:
                break
            for e31 in range(E31+1):
                lognum31 = lognum37 + e31 * log31
                if lognum31 > LOGSQRT:
                    break
                for e29 in range(E29+1):
                    lognum29 = lognum31 + e29 * log29
                    if lognum29 > LOGSQRT:
                        break
                    for e23 in range(E23+1):
                        lognum23 = lognum29 + e23 * log23
                        if lognum23 > LOGSQRT:
                            break
                        for e19 in range(E19+1):
                            lognum19 = lognum23 + e19 * log19
                            if lognum19 > LOGSQRT:
                                break
                            for e17 in range(E17+1):
                                lognum17 = lognum19 + e17*log17
                                if lognum17 > LOGSQRT:
                                    break
                                for e13 in range(E13+1):
                                    lognum13 = lognum17 + e13*log13
                                    if lognum13 > LOGSQRT:
                                        break
                                    for e11 in range(E11+1):
                                        lognum11 = lognum13 + e11*log11
                                        if lognum11 > LOGSQRT:
                                            break
                                        for e7 in range(E7+1):
                                            lognum7 = lognum11 + e7*log7
                                            if lognum7 > LOGSQRT:
                                                break
                                            for e5 in range(E5+1):
                                                lognum5 = lognum7 + e5*log5
                                                if lognum5 > LOGSQRT:
                                                    break
                                                for e3 in range(E3+1):
                                                    lognum3 = lognum7 + e3*log3
                                                    if lognum3 > LOGSQRT:
                                                        break
                                                    for e2 in range(E2+1):
                                                        lognum2 = lognum3 + e2*log2
                                                        if lognum2 > LOGSQRT:
                                                            break

                                                        divA = (e2+1)*(e3+1)*(e5+1)*(e7+1)*(e11+1)*(e13+1)*(e17+1)*(e19+1)*(e23+1)*(e29+1)*(e31+1)*(e37+1)
                                                        divB = (E2+1-e2)*(E3+1-e3)*(E5+1-e5)*(E7+1-e7)*(E11+1-e11)*(E13+1-e13)*(E17+1-e17)*(E19+1-e19)*(E23+1-e23)*(E29+1-e29)
                                                        divB *= (E31-e31+1)*(E37-e37+1)

                                                        if divB < divA:
                                                            break

                                                        hits += 1
                                                        if divA == divB:
                                                            A  = 2**e2 * 3**e3 * 5**e5 * 7**e7 * 11**e11 * 13**e13 * 17**e17 * 19**e19 * 23**e23 * 29**e29 * 31**e31 * 37**e37
                                                            B  = 2**(E2-e2) * 3**(E3-e3) * 5**(E5-e5) * 7**(E7-e7) * 11**(E11-e11) * 13**(E13-e13) * 17**(E17-e17)
                                                            B *= 19**(E19-e19) * 23**(E23-e23) * 29**(E29-e29) * 31**(E31-e31) * 37**(E37-e37)
                                                            if A < B:
                                                                res += 1


        return res


# Main code:
if __name__ == "__main__":
    P = p598()
    P.run()

# Python 3.6.2 times (Burns)
#
#    n      res(n)  function  time (ms)
#   10           3        f0        0.3
#
#   10           3        f1          0.6
#   20         136        f1         96
#   30        1655        f1       5200
#   35        6674        f1      39300
#
#   20         136        f2         37.0
#
#   30        1656        f3       2700
#
#   10           3        f5          0.5
#   20         136        f5         22.9
#   30        1656        f5        788
#   35        6674        f5       3000
#   40       38901        f5       9200
#   45       88592        f5      52100
#   50      662019        f5     159600
#
#   10           3        f6          0.5
#   20         136        f6         23.6
#   30        1656        f6        698
#   35        6674        f6       2500
#   40       38901        f6       7700
#   45       88592        f6      46500
#   50      662019        f6     128800
#
#   30        1656        f7       1975
#
#   30        1656        f8       1524
#
#   30        1656        f9       1773
#   35        6674        f9      12400
#   40       38901        f9      78100
