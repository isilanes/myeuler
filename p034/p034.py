def f1():
    fac = { '0' : 1,
            '1' : 1,
            '2' : 2,
            '3' : 6,
            '4' : 24,
            '5' : 120,
            '6' : 720,
            '7' : 5040,
            '8' : 40320,
            '9' : 362880 }

    suma = 0
    for i in range(3,7*fac['9']):
        digs = str(i)
        facs = [ fac[x] for x in digs ]
        if sum(facs) == i:
            suma += i

    return suma

#-------------------------------------------------------------------------#

res = f1()
print(res)
