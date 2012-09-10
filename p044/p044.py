def f1(max):

    pentas = [ n*(3*n-1)/2 for n in range(max) ]

    for i in range(1,max):
        for j in range(i+1,max):
            pi = pentas[i]
            pj = pentas[j]
            if pi + pj in pentas:
                if pj - pi in pentas:
                    return i, j, pj - pi

    return False

#-------------------------------------------------------------------------#
def f2(max):

    p = {}
    pentas = [ n*(3*n-1)/2 for n in range(max) ]
    for n in pentas:
        p[n] = True

    for i in range(1,max):
        for j in range(i+1,max):
            pi = pentas[i]
            pj = pentas[j]
            if pi + pj in p:
                if pj - pi in p:
                    return i, j, pj - pi

    return False

#-------------------------------------------------------------------------#

res = f2(3000)
print(res)
