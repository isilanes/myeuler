'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

#------------------------------------------------------------------------------#

def f1(nth):
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

    return primes

#------------------------------------------------------------------------------#

for i in range(1):
    res = f1(10001)

print(res[-1])
