def f1():
    i = 1
    string = '0'
    while True:
        string += str(i)
        i += 1
        if len(string) > 1000000:
            break

    res = 1
    for i in [1,10,100,1000,10000,100000,1000000]:
        res *= int(string[i])

    return res

#-------------------------------------------------------------------------#

res = f1()
print(res)
