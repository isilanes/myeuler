#--------------------------------------------------------------------#

def f0():
    '''
    This f0() is not a solution, is just the solution to the 3-gon.
    '''
    print("--- f0 ---")

    import itertools as it

    class Tgon(object):
        
        def __init__(self):
            self.aspas = [None, None, None]
            self.leads = []
        
        def assign(self, list):
            self.aspas[0] = list[:2] + list[3:4]
            self.aspas[1] = list[2:4] + list[5:6]
            self.aspas[2] = list[4:] + list[1:2]
            self.leads = [ list[0], list[2], list[4] ]

        def string(self):
            s = ''
            for aspa in self.aspas:
                s += ''.join([ str(x) for x in aspa ])
            return int(s)

        def isvalid(self):
            '''
            Check whether current setup is valid, returning True
            if so. If invalid, return False ASAP.
            '''
            if self.leads[0] == min(self.leads):
                return sum(self.aspas[0]) == sum(self.aspas[1]) == sum(self.aspas[2])
            return False

    max_string = 0
    T = Tgon()
    for combo in it.permutations(range(1,7), 6):
        T.assign(combo)
        if T.isvalid():
            if T.string() > max_string:
                max_string = T.string()

    print(max_string)

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    import itertools as it

    class Pgon(object):
        
        def __init__(self):
            self.aspas = [None, None, None, None, None]
            self.leads = []
        
        def assign(self, list):
            self.aspas[0] = [ list[0], list[1], list[3] ]
            self.aspas[1] = [ list[2], list[3], list[5] ]
            self.aspas[2] = [ list[4], list[5], list[7] ]
            self.aspas[3] = [ list[6], list[7], list[9] ]
            self.aspas[4] = [ list[8], list[9], list[1] ]
            self.leads = [ list[0], list[2], list[4], list[6], list[8] ]

        def string(self):
            s = ''
            for aspa in self.aspas:
                s += ''.join([ str(x) for x in aspa ])
            return int(s)

        def isvalid(self):
            '''
            Check whether current setup is valid, returning True
            if so. If invalid, return False ASAP.
            '''

            if not 10 in self.leads:
                return False

            if self.leads[0] == min(self.leads):
                s = sum(self.aspas[0])
                for i in range(1,5):
                    if sum(self.aspas[i]) != s:
                        return False
                return True
            return False

    P = Pgon()
    max_string = 0
    # Recall that the first digit of the solution *must* be 6:
    for combo in it.permutations([1,2,3,4,5,7,8,9,10], 9):
        combo = (6,) + combo
        P.assign(combo)
        if P.isvalid():
            if P.string() > max_string:
                max_string = P.string()

    print(max_string)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0():   8.6 ms (not a solution)
# f1(): 250 ms
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
