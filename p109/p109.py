#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    singles = [ [x, 'S{0:d}'.format(x)] for x in range(1,21) + [25] ]
    doubles = [ [2*x, 'D{0:d}'.format(x)] for x in range(1,21) + [25] ]
    triples = [ [3*x, 'T{0:d}'.format(x)] for x in range(1,21) ]

    # Dictionary of score -> combos, where "combos" are the 
    # combinations that result in a score of "score"
    success = {}

    # Checkout in a single shot, must be a double:
    for shot1 in doubles:
        score, combo = shot1
        combo = [combo]
        try:
            success[score].append(combo)
        except:
            success[score] = [ combo ]

    # Checkout in two shots, second must be a double:
    for shot1 in singles + doubles + triples:
        score1, combo1 = shot1
        for shot2 in doubles:
            score2, combo2 = shot2
            score = score1 + score2
            combo = [combo1, combo2]
            try:
                success[score].append(combo)
            except:
                success[score] = [combo]

    # Checkout in three shots, third must be a double:
    for shot1 in singles + doubles + triples:
        score1, combo1 = shot1
        for shot2 in singles + doubles + triples:
            score2, combo2 = shot2
            for shot3 in doubles:
                score3, combo3 = shot3
                score = score1 + score2 + score3
                combo = [combo1, combo2, combo3]
                try:
                    success[score].append(combo)
                except:
                    success[score] = [combo]

    # Now recall that all three-shot scores of the type A-B-DX
    # are equivalent to B-A-DX, so we need to account for that before
    # giving the final answer:
    tot = 0
    for N in range(2,100):
        res = []
        for combo in success[N]:
            if len(combo) < 3:
                res.append(combo)
            else:
                c = combo[:2]
                c.sort()
                combo = c + [combo[-1]]
                if not combo in res:
                    res.append(combo)

        tot += len(res)

    # Final result:
    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 0.7 s (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
