def f1():
    # Binary 1, 11, 101, and 111 are palindromic in base 10 too, because
    # they have 1 digit in base 10 (1, 3, 5 and 7):
    palindromes = [ 1, 3, 5, 7 ]

    # The rest of the palindromes must be (in base 2) of the form:
    #
    # 1abcXcba1
    #
    # where "abc" is a number from zero to 9 binary digits, "abc" is its
    # reversed form, and X is either nothing, zero or one.

    for X in ['', '0', '1']:
        for i in range(512):
            bi = bin(i)[2:]
            # Take into account leading zeros cases in "abc":
            for j in range(len(bi), 10):
                abc = bi.zfill(j)
                
                b = '0b1' + abc + X + abc[::-1] + '1' # (1)
                d = int(b,2)

                if d > 1000000:
                    break
                
                # b is palindromic by construction, but... is d?
                sd = str(d)
                if sd == sd[::-1]:
                    palindromes.append(d)

    return sum(palindromes)

    # (1) x[::-1] returns string x reversed:
    # http://stackoverflow.com/questions/931092/reverse-a-string-in-python

#-------------------------------------------------------------------------#

res = f1()
print(res)
