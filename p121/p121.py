#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    # Let's call p(B,R) the probability that we get B blue extractions
    # and R red extractions (B+R = number of extractions, obviously).
    # After 15 extractions, the probability of winning (i.e. more
    # blue extractions than red extractions), is the sum of prob p(B,R)
    # for all B > R (that is, B = 15..8).
    
    # Denominator:
    deno = 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16 # 16!, actually

    # For red picks, the probability numerator is i, for ith 
    # extraction. For blue picks, the prob numerator is 1, for any
    # extraction.
    numer = 1 # all-blue case (p(15,0) = 1/deno
    for R in range(1,8): # sum all cases of p(B,R) where R < 8
        for combo in it.combinations(range(1,16), R):
            # Each combo is a collection of R indices {Ri}, meaning
            # a red disk was extracted at Ri-th extractions.
            p = 1
            for c in combo:
                p = p * c
            numer += p

    ratio = int(deno/float(numer))
    print(ratio)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 10 ms (python3)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
