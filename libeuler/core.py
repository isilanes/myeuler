# Standard libs:
import sys
import math
import argparse
from datetime import datetime


# Constants:
DEFAULT_F = "0" # which function to run, default first (zero)
DEFAULT_N = "1" # what argument to pass to function(s), default 1


# Functions:
def parse_args(args=sys.argv[1:]):
    """Read and parse arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--functions",
                        help="Comma-separated list of integers i, j..., to run functions fi,\
                                            fj... Default: {d}.".format(d=DEFAULT_F),
                        default=DEFAULT_F)

    parser.add_argument("-n", "--nvals",
                        help="Comma-separated list of integers n, m..., to run functions fi(n),\
                                            fi(m)... Default: {d}.".format(d=DEFAULT_N),
                        default=DEFAULT_N)

    return parser.parse_args(args)


def factors_of(n):
    """Return list of prime factors of n.
    Factors appear repeated if appropriate.
    """
    factors = []

    # Check factor 2:
    while not n % 2:
        factors.append(2)
        n /= 2

    # All the rest (odd):
    factor = 3
    while n > 1:
        if not n % factor:
            factors.append(factor)
            n /= factor
        else:
            factor += 2  # recall N will always be prime (think about it)
            if factor*factor > n: # if so, the remainder N is prime already
                factors.append(int(n))
                break

    return factors


def factors_of_with_primes(n, primes):
    """Return list of prime factors of n.
    Factors appear repeated if appropriate, and are taken from
    given list of primes.
    """
    factors = []

    # Check factor 2:
    while not n % 2:
        factors.append(2)
        n /= 2

    # All the rest (odd):
    i_factor = 1  # i_factor-th prime in list (0 -> 2, 1 -> 3, etc)
    while n > 1:
        prime = primes[i_factor]
        if not n % prime:
            factors.append(prime)
            n /= prime
        else:
            i_factor += 1
            prime = primes[i_factor]
            if prime*prime > n: # if so, the remainder N is prime already
                factors.append(int(n))
                break

    return factors


def gcd(n, m):
    """Greatest common divisor of integers n and m.
    Uses Euclid's algorithm.
    """
    # For convenience, order such that n > m:
    if n < m:
        n, m = m, n

    rem = n % m
    if rem:
        return gcd(m, rem)
    else:
        return m


def lcm(n, m):
    """Least common multiple of integers n and m.
    Uses reduction by the GCD.
    """

    # Use divide-first, and divide by largest first, to avoid potential overflows:
    if n > m:
        return n // gcd(n, m) * m
    else:
        return m // gcd(n, m) * n


def lcm_of_many(number_list):
    """Least common multiple of all the integers in 'number_list'."""

    if not number_list:
        return None
    
    if len(number_list) == 1:
        return number_list[0]

    _lcm = 1
    for number in number_list:
        _lcm = lcm(_lcm, number)

    return _lcm


def is_prime(n):
    """Returns True if n is prime. False otherwise."""

    if n == 2:
        return True

    if not n % 2:
        return False

    for d in range(3, int(math.sqrt(n))+1, 2):
        if not n % d:
            return False

    return True


def run_functions(all_functions):
    """Perform a run of all pertinent solutions."""

    # Parse command-line arguments:
    opts = parse_args()

    # List of functions:
    function_indices = []
    if opts.functions:
        function_indices = [int(i) for i in opts.functions.split(",")]

    # List of N values:
    ns = []
    if opts.nvals:
        ns = [int(i) for i in opts.nvals.split(",")]

    # Execute all functions with all N values:
    times = []
    for i in function_indices:
        for n in ns:
            now = datetime.now()

            print("--- f{i}({n}) ---".format(i=i, n=n))  # print function name

            print(all_functions[i](n))

            dt = (datetime.now() - now).total_seconds()
            times.append([[i,n], dt])

    # Print out times:
    print("\nTimes:\n")
    for (i,n),t in times:
        if t < 2:
            print('f{i}({n}): {t:.1f} ms'.format(i=i, t=t*1000, n=n))
        else:
            print('f{i}({n}): {t:.1f} s'.format(i=i, t=t, n=n))


# Classes:
class FunctionSet(object):
    """Parent class for all solution sets."""

    # Constructor:
    def __init__(self, disp=True):
        self.disp = disp

    # Public methods:
    def f0(self, n):
        """f(i) should be the solutions proposed."""

        raise NotImplementedError

    def run(self):
        """Perform a run of all pertinent solutions."""

        # Parse command-line arguments:
        self.opts = parse_args()

        # List of functions:
        fis = []
        if self.opts.functions:
            fis = [int(i) for i in self.opts.functions.split(",")]

        # List of N values:
        ns = []
        if self.opts.nvals:
            ns = [int(i) for i in self.opts.nvals.split(",")]

        # Execute all functions with all N values:
        times = []
        for i in fis:
            for n in ns:
                now = datetime.now()

                if self.disp:
                    print("--- f{i}({n}) ---".format(i=i, n=n)) # print function name

                fun = getattr(self, "f{}".format(i))
                ret = fun(n)

                if self.disp:
                    print(ret)

                dt = (datetime.now() - now).total_seconds()
                times.append([[i,n], dt])

        # Print out times:
        print("\nTimes:\n")
        for (i,n),t in times:
            if t < 2:
                print('f{i}({n}): {t:.1f} ms'.format(i=i, t=t*1000, n=n))
            else:
                print('f{i}({n}): {t:.1f} s'.format(i=i, t=t, n=n))

