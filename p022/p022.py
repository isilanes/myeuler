'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

#-------------------------------------------------------------------------#

def f1(fn):
    # Read input file:
    with open(fn, 'r') as f:
        names = []
        for line in f:
            line = line.replace('"','')
            aline = line.split(',')
            names.extend(aline)

    # Sort names:
    names.sort()

    # Letter values:
    import string
    i = 1
    value = {}
    for letter in string.ascii_uppercase:
        value[letter] = i
        i += 1

    i = 1
    score = 0
    for name in names:
        worth = 0
        for letter in name:
            worth += value[letter]
        score += worth * i
        i += 1

    return score

#-------------------------------------------------------------------------#

res = f1('names.txt')

print(res)
