def f1(side):
    sum = 1
    for i in range(3, side+1, 2):
        mx = i * i
        d = i - 1
        sum += mx
        for j in range(3):
            mx -= d
            sum += mx

    return sum

#-------------------------------------------------------------------------#

def f2(side):
    sum = 1
    for i in range(3, side+1, 2):
        sum += 4 * i * i - 6 * i - 6

    return sum

#-------------------------------------------------------------------------#

res = f2(1001)

print(res)
