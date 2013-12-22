#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    facs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    def facdigs(N, facs):
        '''
        Take a number N and return the sum of the factorials of
        their digits.
        '''

        digs = [ facs[int(x)] for x in str(N) ]
        return sum(digs)
    
    Nmax = 1000*1000

    n60 = 0
    for N in range(Nmax):
        loop = []
        next = facdigs(N, facs)
        while not next in loop:
            loop.append(next)
            next = facdigs(next, facs)
        if len(loop) == 59:
            n60 += 1
            
    print(n60)

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    facs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    def facdigs(N, facs):
        '''
        Take a number N and return the sum of the factorials of
        their digits.
        '''

        digs = [ facs[int(x)] for x in str(N) ]
        return sum(digs)
    
    Nmax = 1000*1000

    fd = {}
    n60 = 0
    for N in range(Nmax):
        loop = []
        try:
            next = fd[N]
        except:
            next = facdigs(N, facs)
            fd[N] = next
        while not next in loop:
            loop.append(next)
            try:
                next = fd[next]
            except:
                nx = facdigs(next, facs)
                fd[next] = nx
                next = nx
        if len(loop) == 59:
            n60 += 1
            
    print(n60)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): ~ 29 s
# f1(): ~ 3.4 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
