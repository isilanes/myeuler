def f1():
    pandis = []

    # Try 9x numbers:
    for i in range(1,9):
        m = 90 + i
        digits = []
        for n in range(1,6):
            r = m * n
            repeated = False
            for c in str(r):
                if c in digits:
                    repeated = True
                    break
                else:
                    digits.append(c)

            if repeated:
                break

        if len(digits) == 9 and '0' not in digits:
            pandis.append(int(''.join(digits)))

    # Try 9xx numbers:
    for i in range(1,88):
        m = 900 + i
        digits = []
        for n in range(1,4):
            r = m * n
            repeated = False
            for c in str(r):
                if c in digits:
                    repeated = True
                    break
                else:
                    digits.append(c)

            if repeated:
                break

        if len(digits) == 9 and '0' not in digits:
            pandis.append(int(''.join(digits)))

    # Try 9xxx numbers:
    for i in range(1,877):
        m = 9000 + i
        digits = []
        for n in range(1,4):
            r = m * n
            repeated = False
            for c in str(r):
                if c in digits:
                    repeated = True
                    break
                else:
                    digits.append(c)

            if repeated:
                break

        if len(digits) == 9 and '0' not in digits:
            pandis.append(int(''.join(digits)))

    return max(pandis)

#-------------------------------------------------------------------------#

res = f1()
print(res)
