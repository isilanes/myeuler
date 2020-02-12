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
from libeuler import core


class p387(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n=14):
        """Only slightly clever solution, fast enough."""

        # Generate length-n Harshads from lenght-n-1s:
        harshads = {
            1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        }
        strong_harshads = []
        for ndigits in range(2, n):
            curr = []
            for pre_har in harshads[ndigits-1]:
                digit_sum_pre_har = sum([int(d) for d in str(pre_har)])
                for i in range(10):
                    har = pre_har * 10 + i
                    digit_sum = digit_sum_pre_har + i
                    if not har % digit_sum:
                        curr.append(har)
                        ratio = har // digit_sum
                        if core.is_prime(har//digit_sum):
                            strong_harshads.append(har)

            harshads[ndigits] = curr

        # From all strong, right-truncatable Harshads, pick the ones that give rise to a prime 
        # when single digit is attached to its right side:
        total = 0
        for strong_harshad in strong_harshads:
            for digit in range(10):
                candidate = strong_harshad * 10 + digit
                if core.is_prime(candidate):
                    total += candidate

        return total


# Main code:
if __name__ == "__main__":
    P = p387()
    P.run()

# Benchmarks:
benchmarks = {
    "Python 3.5.2 (Skinner)": {
        "f0": {
            "skip": False,
            "data": [ # n, result, time (ms)
                [ 10**2,                0,     0.01 ],
                [ 10**4,            90619,     0.3 ],
                [ 10**6,          1188721,     1.1 ],
                [ 10**8,        130459097,     7.4 ],
                [ 10**10,     36498117748,    36.5 ],
                [ 10**12,   2897368636255,   337.2 ],
                [ 10**14, 696067597313468,  5300 ],
            ],
        },
    },
    "PyPy 5.2.1 (Skinner)": {
        "f0": {
            "skip": False,
            "data": [ # n, result, time (ms)
                [ 10**2,                0,     0.1 ],
                [ 10**4,            90619,     0.6 ],
                [ 10**6,          1188721,     3.9 ],
                [ 10**8,        130459097,    11.2 ],
                [ 10**10,     36498117748,    28.8 ],
                [ 10**12,   2897368636255,    72.1 ],
                [ 10**14, 696067597313468,   759.9 ],
            ],
        },
    },
}
