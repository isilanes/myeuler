def f1():
    prod_nums = 1
    prod_dens = 1
    for i in range(10,100):
        if not i % 10:
            continue
        di = str(i)
        for j in range(10,i):
            if not j % 10:
                continue
            dj = str(j)
            for d in di:
                if d in dj:
                    ni = int(di.replace(d,'',1))
                    nj = int(dj.replace(d,'',1))
                    if ni/nj == i/j:
                        prod_nums = prod_nums * j
                        prod_dens = prod_dens * i
                        break

    frac = prod_nums/prod_dens
    prod = frac
    i = 1
    while prod % 1:
        i += 1
        prod = frac * i

    return i

#-------------------------------------------------------------------------#

res = f1()
print(res)
