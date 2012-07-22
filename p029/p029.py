def f1(max):
    uniq = {}
    for a in range(2,max+1):
        for b in range(2,max+1):
            r = a**b
            uniq[r] = True

    return len(uniq)

#-------------------------------------------------------------------------#

res = f1(100)

print(res)
