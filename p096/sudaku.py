class Sudoku(object):
    
    # List of 9 arrays of 9 indices each, where i-th array corresponds
    # to i-th quadrant in grid, and j-th element in i-th array corresponds
    # to j-th index in i-th quadrant:
    quadrants = [
            [0,1,2,9,10,11,18,19,20],
            [3,4,5,12,13,14,21,22,23],
            [6,7,8,15,16,17,24,25,26],
            [27,28,29,36,37,38,45,46,47],
            [30,31,32,39,40,41,48,49,50],
            [33,34,35,42,43,44,51,52,53],
            [54,55,56,63,64,65,72,73,74],
            [57,58,59,66,67,68,75,76,77],
            [60,61,62,69,70,71,78,79,80],
            ]

    def __init__(self):
        # Array where i-th element is a 1-to-9 digit string, containing all
        # potentially valid values for i-th cell in grid. Varies in time
        # until all cells have a 1-digit value (solution):
        self.cells = [ '123456789' for i in range(81) ]

        # Array where i-th element is a 1-to-9 digit string, containing all
        # potentially valid values for i-th cell in grid JUST AFTER reading
        # input. This means the values here are IMMUTABLE once set at beginning.
        self.icells = [ None for i in range(81) ]

        # Array of indices that are not assigned in input. These are the only
        # cells we will operate on after reading input.
        self.vacants = []

        # Opposite of self.vacants. The self.cells[j] values for j in this
        # array will change over time:
        self.originals = []

        # Dictionaries of i -> L, where L is list of indices of cells affected
        # by i (i.e. in the same row/column/sector as cell i). Notice values i
        # n self.originals are not included in L, as they will be immutable.
        self.affects = {}
    
    def read(self, fn):
        '''
        Read data from file, and initialize accordingly.
        '''

        # Read from file:
        with open(fn) as f:
            i = 0
            for line in f:
                line = line.strip()
                for e in line.split():
                    if e == '0':
                        # Then this cell is not defined in input:
                        self.vacants.append(i)
                    else:
                        # The value for this cell is given in the input:
                        self.originals.append(i)

                        # Remember: this array is mutable. However it won't change
                        # for those particular i-s:
                        self.cells[i] = e
                        
                    i += 1

        # Initialize self.affects dictionary:

        # Same quadrant:
        for q in self.quadrants:
            for i in q:
                self.affects[i] = [ x for x in q if x != i and x in self.vacants ]

        for i in range(81):
            r = i // 9
            c = i % 9

            # Same row:
            self.affects[i].extend([ x for x in range(r*9, (r+1)*9) if x in self.vacants ])

            # Same column:
            self.affects[i].extend([ x for x in range(c,81,9) if x in self.vacants ])

            # Avoid duplicity:
            self.affects[i] = set(self.affects[i])
            if i in self.affects[i]:
                self.affects[i].remove(i)

        # Initialize cells removing options forbidden by input values:
        for i in self.originals:
            v = self.cells[i]
            # Leaves self.cells[i] as it was, but its side effects
            # do what we need them to:
            self.assign(i, v)

        # Populate self.icells with a copy of the initial self.cell,
        # containing initial, immutable, values defined by input:
        self.icells = self.cells[:]
    
    def loop(self):
        # The i-th value on this array holds the value asigned so far (guessed)
        # for i-th vacant cell:
        guessed = []

        # The i-th value on this array holds an index j for i-th vacant cell, where
        # j stands for the j-th possible (among the ones still possible) value for
        # cell i, which is the current guess for i-th cell:
        jth = [ 0 for x in self.vacants ]

        i = 0 # index of vacant cell we are on
        for kk in range(1):
            iv = self.vacants[i] # index of current cell whithin cells
            print iv

            # Choose first "valid" value among still possible ones on i-th vacant cell:
            j = jth[i]
            val = self.cells[iv][j]
            self.assign(iv, val)

    def write(self):
        '''
        Print out the current state of the grid.
        '''

        print("---")
        for i in range(9):
            string = ''
            for e in self.cells[i*9:(i+1)*9]:
                string += '{0:10s}'.format(e)
            print(string)

    def assign(self, i, val):
        '''
        Assign value "val" to cell "i", which triggers elimination
        of "val" from list of possible values for all other cells
        in same column, row and sector.
        '''

        self.cells[i] = val

        for j in self.affects[i]:
            self.cells[j] = self.cells[j].replace(val,'')

S = Sudoku()
S.read("example.sud")
S.write()
S.loop()
S.write()

