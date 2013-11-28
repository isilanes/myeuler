#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    win1 = 0
    with open("poker.txt") as f:
        for line in f:
            aline = line.split()
            h1 = aline[:5]
            h2 = aline[5:]
            if hand_quality(h1) > hand_quality(h2):
               win1 += 1

    print win1

#--------------------------------------------------------------------#

def hand_quality(hand):
    '''
    Take a hand in [8C, TS, KC, 9H, 4S] format, and return a quality
    string, according to following scheme (in all cases Nx is 02 to 14,
    for 2 to ace):

    High card:       01.N1.N2.N3.N4.N5
                     N1 being highest card, N5 lowest
    One pair:        02.N1.N2.N3.N4
                     N1 being the pair card, 
                     N2-N4 other three, highest to lowest
    Two pairs:       03.N1.N2.N3
                     N1 being the highest pair card,
                     N2 the lowest pair card,
                     N3 the last card
    Three of a kind: 04.N1.N2.N3
                     N1 being the trio card,
                     N2 and N3 remaining highest and lowest
    Straight:        05.N1
                     N1 being the highest card
    Flush:           06.N1.N2.N3.N4.N5
                     N1 to N5 being highest to lowest card
    Full house:      07.N1.N2
                     N1 being the trio card, and N2 the duo one
    Four of a kind:  08.N1.N2
                     N1 being the poker card, N2 the remaining one
    Straight flush:  09.N1
                     N1 being the highest card
    Royal flush:     sub-case of straight flush (09.14)
    '''

    val2val = {
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'T' : 10,
            'J' : 11,
            'Q' : 12,
            'K' : 13,
            'A' : 14,
            }

    h = []
    for card in hand:
        v = val2val[card[0]] # value
        c = card[1] # color
        h.append([v,c])

    flush = False
    straight = False

    # Flush?:
    if h[0][1] == h[1][1] == h[2][1] == h[3][1] == h[4][1]:
        flush = True

    # Straight?:
    vs = [ x[0] for x in h ]
    vs.sort()
    if vs[0] == vs[1] - 1 == vs[2] - 2 == vs[3] - 3 == vs[4] - 4:
        straight = True
    elif vs[0] == 2 and vs[-2] == 5 and vs[-1] == 14:
        # Special case where ace is played as a "1",
        # to complete the straight.
        straight = True

    if flush:
        if straight:
            # If highest valued card is Ace, not necessarily
            # is it royal flush, because (see above) we also
            # consider A,2,3,4,5 to be straight flush:
            if vs[0] == 2 and vs[-1] == 14:
                # Then A2345 straight, ordered as 2345A, which
                # is a straight to the 5, not Ace.
                code = '09.{0:02d}'.format(vs[-2])
            else:
                code = '09.{0:02d}'.format(vs[-1])
            return code
        else: # it's a non-straight flush, can't be a full house
            code = [ '{0:02d}'.format(x) for x in vs ]
            code.sort()
            code.reverse()
            code = '06.' + '.'.join(code)
            return code
    elif straight: # a non-flush straight
        # See straight flush above:
        if vs[0] == 2 and vs[-1] == 14:
            return '05.05'
        else:
            return '05.{0:02d}'.format(vs[-1])
    else:
        abundance = {}
        for v in vs:
            try:
                abundance[v] += 1
            except:
                abundance[v] = 1

        reverse_ab = {}
        ones = []
        code = "01."
        for k,v in abundance.items():
            if v == 1:
                ones.append(k)
            elif v in reverse_ab: # then two pairs
                ps = [ reverse_ab[v], k]
                ps.sort()
                code = '03.{0[1]:02d}.{0[0]:02d}.'.format(ps)
            else:
                reverse_ab[v] = k

        r = reverse_ab.keys()
        if len(r) == 2: # must be full house
            code = '07.{0[3]:02d}.{0[2]:02d}'.format(reverse_ab)
        elif len(r) == 1: # either pair, 3-of-a-kind, or poker
            if r[0] == 4: # poker
                code = '08.{0[4]:02d}.'.format(reverse_ab)
            elif r[0] == 3: # 3-of-a-kind
                code = '04.{0[3]:02d}.'.format(reverse_ab)
            elif r[0] == 2:
                # pair, but only if not two-pair:
                if len(ones) == 3:
                    code = '02.{0[2]:02d}.'.format(reverse_ab)

        # Add extra cards:
        ones.sort()
        ones.reverse()
        ones = [ '{0:02d}'.format(x) for x in ones ]
        code += '.'.join(ones)

        return code

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 0.4 s
