def f1():
    import itertools

    # M x N = O, M,N,O being 1-9 pandigital
    pandi = '123456789'

    pandis = {}
    for m in range(1,3):
        for e in itertools.permutations(pandi, m):
            M = ''.join(e)
            rem = [ x for x in pandi if not x in M ]
            for n in range(m,int(4.5-m/2)+1):
                for el in itertools.permutations(rem, n):
                    N = ''.join(el)
                    REM = [ x for x in rem if not x in N ]
                    MN = int(M) * int(N)
                    MN = [ x for x in str(MN) ]
                    MN.sort()
                    if MN == REM:
                        A = int(M)
                        B = int(N)
                        C = A*B
                        pandis[C] = [A, B] 

    sum = 0
    for pan in pandis:
        sum += pan

    return sum

#-------------------------------------------------------------------------#

res = f1()
print(res)
