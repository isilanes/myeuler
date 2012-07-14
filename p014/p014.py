'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

#-------------------------------------------------------------------------#

def f1(nmax):
    max_i = 2 # number with max steps
    max_s = 1 # how many of them
    steps = {}
    for i in range(3,nmax,2):
        num = i
        nsteps = 0
        while num > 1:
            if num % 2: # odd
                num = 3 * num + 1
            else: # even
                num = num / 2
            nsteps += 1

            if num in steps:
                nsteps += steps[num]
                break

        steps[i] = nsteps

        if nsteps > max_s:
            max_i = i
            max_s = nsteps

    return [max_i, max_s]

#-------------------------------------------------------------------------#

def f2(nmax):
    max_i = 2 # number with max steps
    max_s = 1 # how many of them
    steps = {}
    for i in range(3,nmax,2):
        num = i
        nsteps = 0
        while num > 1:
            if num % 2: # odd
                # Any odd number produces an even number (3n+1 = even
                # if n odd), so we do two steps at once:
                num = (3 * num + 1)/2
                nsteps += 2
            else: # even
                num = num / 2
                nsteps += 1

            if num in steps:
                nsteps += steps[num]
                break

        steps[i] = nsteps

        if nsteps > max_s:
            max_i = i
            max_s = nsteps

    return [max_i, max_s]

#-------------------------------------------------------------------------#

res = f2(1000000)

print(res)
