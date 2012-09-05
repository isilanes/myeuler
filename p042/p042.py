def f1():
    words = file2list('words.txt')

    # Find max word value, and save words and their word values in dict:
    max_wv = 0
    wvs = {} # dict with word -> value
    for word in words:
        v = wordvalue(word)
        wvs[word] = v
        if v > max_wv:
            max_wv = v

    # Find triangle numbers up to max word value max_wv:
    n = 1
    t = 1
    triangle = { 1 : True }
    while t < max_wv:
        n += 1
        t = n * (n + 1) / 2
        triangle[t] = True

    # Loop over words, and count how many have triangular wv:
    ntriangular = 0
    for wv in wvs.values():
        if wv in triangle:
            ntriangular += 1

    return ntriangular

#-------------------------------------------------------------------------#

def file2list(fn):
    '''Read file fn, and return list of words.'''

    words = []

    with open(fn,'r') as f:
        for line in f:
            a = line.replace('"','')
            a = a.split(',')
            words.extend(a)

    return words

#-------------------------------------------------------------------------#

def wordvalue(word):
    '''Return word value of word word, e.g.: wordvalue(abc) = 1+2+3 = 6.'''

    val = {}
    i = 1
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        val[letter] = i
        i += 1

    wv = 0
    for letter in word:
        wv += val[letter]

    return wv

#-------------------------------------------------------------------------#

res = f1()
print(res)
