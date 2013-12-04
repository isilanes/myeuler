#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    # Read input:
    cipher = []
    with open("cipher1.txt") as f:
        line = f.readline().strip()
        cipher = [ int(x) for x in line.split(',') ]

    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                K = [ord(a), ord(b), ord(c)]
                nk = len(K)

                res = []
                i = 0
                while True:
                    piece = cipher[nk*i:nk*(i+1)]

                    for p,k in zip(piece,K):
                        letter = chr(operator.xor(p,k))
                        res.append(letter)

                    if len(piece) < nk:
                        break

                    i += 1

                res = ''.join(res)
                if ' the ' in res:
                    print("\n{0}".format(res))
                    ascii_sum = 0
                    for letter in res:
                        ascii_sum += ord(letter)
                    key = ''.join([chr(x) for x in K])
                    print("\nkey = {0}\nsum = {1}".format(key, ascii_sum))
                    return

#--------------------------------------------------------------------#

import string
import timeit
import operator

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 2.8 s
