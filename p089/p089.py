#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")
    
    # Read numbers:
    numlist = []
    with open("roman.txt") as f:
        for line in f:
            num = line.strip()
            numlist.append(num)

    def roman2dec(rom):
        '''
        Take roman numeral rom, and return decimal value.
        '''

        vals = { 
                'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1,
                }

        # Expand subtractive cases:
        rom = rom.replace("IV", "IIII")
        rom = rom.replace("IX", "VIIII")
        rom = rom.replace("XL", "XXXX")
        rom = rom.replace("XC", "LXXXX")
        rom = rom.replace("CD", "CCCC")
        rom = rom.replace("CM", "DCCCC")

        res = 0
        for s in rom:
            res += vals[s]
        return res

    def dec2roman(dec):
        '''
        Take decimal number and return corresponding roman, in
        minimal form.
        '''

        res = ''

        # Thousands:
        n = dec // 1000 # // unconditionally truncates, even in Python 3.x
        res += 'M' * n
        dec -= n*1000

        # 900:
        if dec >= 900:
            res += 'CM'
            dec -= 900

        # 500s (equal to 1000s, but we know there can only be
        # up to one "500", as dec < 1000 by now):
        if dec >= 500:
            res += "D"
            dec -= 500

        # 400:
        if dec >= 400:
            res += 'CD'
            dec -= 400

        # 100s:
        n = dec // 100
        res += 'C' * n
        dec -= n*100

        # 90:
        if dec >= 90:
            res += "XC"
            dec -= 90

        # 50s (like 500s):
        if dec >= 50:
            res += "L"
            dec -= 50

        # 40:
        if dec >= 40:
            res += "XL"
            dec -= 40

        # 10s:
        n = dec // 10
        res += 'X' * n
        dec -= n*10

        # 9:
        if dec == 9:
            res += 'IX'
            return res

        # 5s (like 500s):
        if dec >= 5:
            res += "V"
            dec -= 5

        # 4:
        if dec == 4:
            res += 'IV'
            return res

        # 1s:
        res += 'I' * dec

        return res

    def minimal(rom):
        '''
        Take roman numeral rom, and return in minimal form, e.g.:
        XXXX -> XL
        IIII -> IV
        '''

        # Pass rom to decimal:
        dec = roman2dec(rom)

        # Pass dec to minimal rom and return:
        return dec2roman(dec)

    # Loop over all numbers:
    saved = 0
    for num in numlist:
        m = minimal(num)
        saved += len(num) - len(m)

    print(saved)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: 8 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
