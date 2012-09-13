def f1():
    import math

    n = 143
    while True:
        n += 1

        # Hexagonal number for index n:
        h = n * (2*n - 1)

        # Is it triangular?:
        # Do not test, as all hexagonals are triangular
        #m = math.sqrt(2*h + 0.25) - 0.5
        #if m % 1:
        #    continue

        # Is it pentagonal
        m = 1.0/6 + math.sqrt(6*h + 0.25)/3.0
        if m != int(m):
            continue
       
        return h

#-------------------------------------------------------------------------#

res = f1()
print(res)
