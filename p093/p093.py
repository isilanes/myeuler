#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import parser
    import itertools as it

    def parens(arr, op1, op2, op3):
        '''
        Return all possible parenthesizations (11) for arr and op*.
        '''

        a, b, c, d = arr

        res = []
        res.append(a + op1 + b + op2 + c + op3 + d)
        res.append("(" + a + op1 + b + op2 + c + ")" + op3 + d)
        res.append("(" + a + op1 + b + ")" + op2 + c + op3 + d)
        res.append(a + op1 + "(" + b + op2 + c + op3 + d + ")")
        res.append(a + op1 + "(" + b + op2 + c + ")" + op3 + d)
        res.append(a + op1 + b + op2 + "(" + c + op3 + d + ")")
        res.append("((" + a + op1 + b + ")" + op2 + c + ")" + op3 + d)
        res.append("(" + a + op1 + "(" + b + op2 + c + "))" + op3 + d)
        res.append("(" + a + op1 + b + ")" + op2 + "(" + c + op3 + d + ")")
        res.append(a + op1 + "((" + b + op2 + c + ")" + op3 + d + ")")
        res.append(a + op1 + "(" + b + op2 + "(" + c + op3 + d + "))")

        return res

    def opers(arr):
        '''
        Take an array of digits arr and produce all combinations 
        of operations possible.
        '''

        res = {}
        # All combinations of operations:
        for op1 in ['+', '/', '-', '*']:
            for op2 in ['+', '/', '-', '*']:
                for op3 in ['+', '/', '-', '*']:
                    # Eleven possible parenthesizations:
                    for eq in parens(arr,op1,op2,op3):
                        code = parser.expr(eq).compile()
                        try:
                            n = eval(code)
                            res[n] = eq
                        except:
                            pass

        return res

    max_max_i = 0
    max_max_c = None
    for arr in it.combinations(range(1,10),4):
        arr = [ str(x) for x in arr ]

        R = {}
        for combo in it.permutations(arr):
            res = opers(combo)
            for r in res:
                R[r] = res[r]

        max_i = 0
        while max_i + 1 in R:
            max_i += 1

        if max_i > max_max_i:
            max_max_i = max_i
            max_max_c = ''.join(arr)
            print(max_max_c, "->", max_max_i)

    string = '\n{1} ({0})'.format(max_max_i, max_max_c)
    print(string)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# python3 is a must, so that i/j divisions are not truncated, but rather
# equal to n=i/j, with n integer if not i % j, and else float.
#
# f0: ~55 s (python3)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
