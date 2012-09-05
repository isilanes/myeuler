def f1():
    import itertools

    tot = 0

    for c in itertools.permutations('0123456789'):
        pandigital = ''.join(c)

        if int(pandigital[3]) % 2:
            continue

        if int(pandigital[7:10]) % 17:
            continue

        if int(pandigital[6:9]) % 13:
            continue

        if int(pandigital[5:8]) % 11:
            continue

        if int(pandigital[4:7]) % 7:
            continue

        if int(pandigital[3:6]) % 5:
            continue

        if int(pandigital[2:5]) % 3:
            continue

        tot += int(pandigital)

    return tot

#-------------------------------------------------------------------------#

res = f1()
print(res)
