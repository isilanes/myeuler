#-------------------------------------------------------------------------#

def f1():
    import itertools

    i = 0
    for element in itertools.permutations(range(10)):
        i += 1
        if i > 999999:
            return ''.join([str(x) for x in element])

#-------------------------------------------------------------------------#

res = f1()

print(res)
