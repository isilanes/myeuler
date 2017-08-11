# Standard libs:
import sys
import math
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p152(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n):
        """Slow solution. I thought it was smart, but it appears to be naïve."""

        def deintegerize(number_list):
            """From numbers (lcm/n)**2, return list of n values."""

            return [int(lcm/math.sqrt(val)) for val in number_list]

        def groups(target, number_list):
            """Return list of all subsets of integers in 'number_list' that add to 'target'."""

            if not number_list: # empty list
                return []

            if sum(number_list) == target:
                return [number_list]

            ret = []
            for i, number in enumerate(number_list):
                if target == number:
                    ret.append([number])
                    continue

                subtarget = target - number
                subnumber_list = number_list[i+1:]
                for group in groups(subtarget, subnumber_list):
                    print("DEBUG40", deintegerize(subgroup))
                    if group:
                        subgroup = [number]
                        subgroup.extend(group)
                        print("DEBUG42", deintegerize(subgroup))
                        ret.append(subgroup)

            return ret


        lcm = core.lcm_of_many(range(2, n))
        elements = [(lcm // e)**2 for e in range(2, n+1)]
        TARGET = lcm**2 // 2

        print(TARGET)
        print(deintegerize(elements))
        g = groups(TARGET, elements)
        for group in g:
            print(group)

    def f1(self, n):
        """Like f0, but sorted in reverse, so some 'clever' assumption can be made.
        number_list must be ordered from smallest to largest.
        """
        def deintegerize(number_list):
            """From numbers (lcm/n)**2, return list of n values."""

            return [int(lcm/math.sqrt(val)) for val in number_list]

        def groups(target, number_list):
            """Return list of all subsets of integers in 'number_list' that add to 'target'."""

            if not number_list: # empty list
                return []

            if number_list[0] > target:
                return []

            if sum(number_list) == target:
                return [number_list]

            ret = []
            for i, number in enumerate(number_list):
                if target == number:
                    ret.append([number])
                    continue

                subtarget = target - number
                subnumber_list = number_list[i+1:]
                for group in groups(subtarget, subnumber_list):
                    print("DEBUG40", deintegerize(subgroup))
                    if group:
                        subgroup = [number]
                        subgroup.extend(group)
                        print("DEBUG42", deintegerize(subgroup))
                        ret.append(subgroup)

            return ret


        lcm = core.lcm_of_many(range(2, n))
        elements = [(lcm // e)**2 for e in range(n, 1, -1)]
        TARGET = lcm**2 // 2

        print(TARGET)
        print(deintegerize(elements))
        g = groups(TARGET, elements)
        for group in g:
            print(group)


# Main code:
if __name__ == "__main__":
    P = p152()
    P.run()

# Python 3.6.2 times (Skinner)
#
#    n      res(n)  function  time (ms)
#
#   35           1        f0         -

