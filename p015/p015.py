#-------------------------------------------------------------------------#

def f1(side):
    # The result is proposed to be:
    #
    # routes = (2n)! / (n!)**2
    routes = 1
    for i in range(side+1, 2*side+1):
        routes = routes * i

    for i in range(2,side+1):
        routes = routes / i

    return int(routes)

#-------------------------------------------------------------------------#

res = f1(20)

print(res)
