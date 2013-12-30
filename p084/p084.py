#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import random

    class Square:

        def __init__(self, goto):
            # Possible outcomes of picking a card in a square. goto
            # is an array of outcomes, where each outcome is the index
            # of the square we would go to. A cell were no card is picked
            # will have [i] as goto value, where i is the index
            # of the square itself.
            self.goto = [goto]

    # Build board:
    board = [ Square(i) for i in range(40) ] # basic squares
    GO = 0
    JAIL = 10
    C1 = 11
    E3 = 24
    H2 = 39
    R1 = 5
    board[2].goto = [GO, JAIL] + 14*[2] # CC1
    board[17].goto = [GO, JAIL] + 14*[17] # CC2
    board[33].goto = [GO, JAIL] + 14*[33] # CC3
    board[7].goto = [GO, JAIL, C1, E3, H2, R1, 15, 15, 12, 4] + 6*[7] # CH1
    board[22].goto = [GO, JAIL, C1, E3, H2, R1, 25, 25, 28, 19] + 6*[22] # CH2
    board[36].goto = [GO, JAIL, C1, E3, H2, R1, 5, 5, 12, 33] + 6*[36] # CH3
    board[30].goto = [JAIL] # G2J

    # Dictionary of #square -> #visits:
    nvisits = {}
    for i in range(40):
        nvisits[i] = 0

    # rolls:
    rolls = [ (x,y) for x in range(1,5) for y in range(1,5) ]

    # Play at random for N rounds:
    curr = GO
    for r in range(1000*1000):
        roll = random.choice(rolls) # first roll
        curr += sum(roll)
        while curr > 39:
            curr -= 40
        curr = random.choice(board[curr].goto)
        nvisits[curr] += 1
        if roll[0] == roll[1]: # if double, roll a second time
            roll2 = random.choice(rolls)
            curr += sum(roll2)
            while curr > 39:
                curr -= 40
            curr = random.choice(board[curr].goto)
            nvisits[curr] += 1

            if roll2[0] == roll2[1]: # if double, roll a third (and last) time
                roll3 = random.choice(rolls)
                if roll3[0] == roll3[1]: # a third double sends us to jail
                    curr = 10
                    nvisits[curr] += 1
                else:
                    curr += sum(roll3)
                    while curr > 39:
                        curr -= 40
                    curr = random.choice(board[curr].goto)
                    nvisits[curr] += 1

    # Results:
    t = sum(nvisits.values())
    deco = [ [y,x] for x,y in nvisits.items() ]
    deco.sort()
    for ns in deco[-1:-6:-1]:
        n, s = ns
        string = '{0:02d} : {1:9.4f}'.format(s, 100*float(n)/t)
        print(string)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 0.7 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
