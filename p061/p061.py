#--------------------------------------------------------------------#

def f1(nmax):
    print("--- f1 ---")

    def get_figurate(sides,n):
        '''
        Return nth sides-sided figurate number (Psides,n).
        '''

        if sides == 3:
            return n*(n+1)/2

        if sides == 4:
            return n*n

        if sides == 5:
            return n*(3*n-1)/2

        if sides == 6:
            return n*(2*n-1)

        if sides == 7:
            return n*(5*n-3)/2

        if sides == 8:
            return n*(3*n-2)

    # Generate all figurate numbers:
    figurates = {}
    for sides in range(3,9):
        figurates[sides] = []
        i = 0
        while True:
            p = get_figurate(sides,i)       
            if p > 9999:
                break
            elif p > 999:
                figurates[sides].append(str(p))
            i += 1

    # Find cycle:
    for piece1 in figurates[8]:
        rem = [ 3, 4, 5, 6, 7 ]
        for i in rem:
            for piece2 in figurates[i]:
                if piece2[:2] == piece1[2:]:
                    print piece1, piece2
                    rem.remove(i)
                    for j in rem:
                        for piece3 in figurates[j]:
                            if piece3[:2] == piece2[2:]:
                                print piece1, piece2, piece3
                                rem.remove(j)
                                for k in rem:
                                    for piece4 in figurates[k]:
                                        if piece4[:2] == piece3[2:]:
                                            print piece1, piece2, piece3, piece4
                                            rem.remove(k)
                                            print rem
                                            for l in rem:
                                                print l
                                                for piece5 in figurates[l]:
                                                    if piece5[:2] == piece4[2:]:
                                                        print i,j,k,l
                                                        rem.remove(l)
                                                        m = rem[0] # last remaining
                                                        piece6 = piece5[2:] + piece1[:2]
                                                        print piece1, piece2, piece3, piece4, piece5,'>',piece6
                                                        if piece6 in figurates[m]:
                                                            print piece1, piece2, piece3, piece4, piece5, piece6
                                                            print 8, i, j, k, l, m
                                                            #total  = int(p8) + int(pi) + int(pj)
                                                            #total += int(pk) + int(pl) + int(pm)
                                                            #print total
                                                            return
                                                        rem.append(l)
                                            rem.append(k)
                                rem.append(j)
                    rem.append(i)

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1(1000)', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # doesn't work
