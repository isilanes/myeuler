def f1():
    tot = 0
    for i in range(1,1000): # this leaves 1000 itself out, on purpose
        tot += i**i

    return str(tot)[-10:]

#--------------------------------------------------------------------#

res = f1()
print(res)
