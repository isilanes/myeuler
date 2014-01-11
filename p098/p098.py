#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")
    
    import math
    import itertools as it

    def issquare(N):
        '''
        Return True if N is a perfect square, false otherwise.
        '''

        s = int(math.sqrt(N))
        return s*s == N
    
    # Read words from file, and save in dictionary by sorted chars
    # (to find anagrams):
    words ={}
    with open("words.txt") as f:
        for line in f:
            ws = line.split(",")
            for w in ws:
                w = w.replace('"','')
                so = ''.join(sorted(w))
                try:
                    words[so].append(w)
                except:
                    words[so] = [w]

    # Loop over possibilities:
    max_sq = 0
    for e in words.keys():
        # Each e has a list of words:
        ws = words[e]
        if len(ws) > 1:
            s = set(e)
            r = len(s)
            for combo in it.permutations('123456789', r):
                squares = []
                for word in ws:
                    N = word
                    for letter,value in zip(s, combo):
                        N = N.replace(letter, value)
                    N = int(N)
                    if issquare(N):
                        squares.append(N)
                if len(squares) > 1:
                    msq = sorted(squares)[-1]
                    if msq > max_sq:
                        max_sq = msq

    print(max_sq)
    
#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 5.5 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
