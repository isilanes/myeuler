def f1():
    maxn = 0
    abmax = [0, 0]
    for a in range(-1000, 1001):
        for b in range(1001):
            n = -1
            while True:
                n += 1
                m = n*n + a*n + b
                if m < 2 or not isprime(m):
                    break

                # n here will be length of series:
                if n > maxn:
                    maxn = n
                    abmax = [a, b]

    return [abmax[0]*abmax[1], abmax]

#-------------------------------------------------------------------------#

def isprime(m):
    import math

    if not m % 2:
        return False

    for i in range(3, int(math.sqrt(m)+1), 2):
        if not m % i:
            return False

    # If we reach so far, it is prime:
    return True

#-------------------------------------------------------------------------#

res = f1()
print(res)
