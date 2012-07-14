'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

#-------------------------------------------------------------------------#

def f1():
    units = { 
            1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine',
            10 : 'ten',
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'nineteen',
            }

    tens = { 
            0 : '',
            2 : 'twenty',
            3 : 'thirty',
            4 : 'forty',
            5 : 'fifty',
            6 : 'sixty',
            7 : 'seventy',
            8 : 'eighty',
            9 : 'ninety',
            }

    letters = 0
    for num in range(1,1000):
        d = [ int(x) for x in '{0:03d}'.format(num) ]
        string = ''
        if d[0]:
            string += '{0} hundred '.format(units[d[0]])

            if d[1] or d[2]:
                string += 'and '

        if d[1] == 1:
            last = d[1] * 10 + d[2]
            string += units[last]
        else:
            string += '{0} '.format(tens[d[1]])

            if d[2]:
                string += units[d[2]]

        string = string.replace(' ','')
        letters += len(string)

    # Add digits of 1000:
    letters += len("onethousand")

    return letters

#-------------------------------------------------------------------------#

res = f1()

print(res)
