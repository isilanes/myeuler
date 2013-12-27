#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    # From: http://en.wikipedia.org/wiki/Partition_(number_theory)

    class MemoP(object):
        
        def __init__(self):
            self.cache = {}

        def call(self,N):
            if not N in self.cache:
                if N < 0:
                    return 0

                if N < 2:
                    return 1

                res = 0
                for k in range(1,N):
                    iplus = N - k*(3*k-1)/2
                    iminus = N - k*(3*k+1)/2
                    if iplus < 0:
                        break
                    res += (-1)**(k-1) * ( self.call(iplus) + self.call(iminus) )

                self.cache[N] = res

            return self.cache[N]
    
    MP = MemoP()
    i = 1
    p = 1
    while p % 1000000:
        i += 1
        p = MP.call(i)

    print(i, p)
    
#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
