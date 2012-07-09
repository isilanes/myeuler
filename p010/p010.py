'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

#------------------------------------------------------------------------------#

def f1(max):
    primes = [2,3]
    i = primes[-1] + 2
    while i < max:
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

    return sum(primes)

#------------------------------------------------------------------------------#

for i in range(1):
    res = f1(2000000)

print(res)
