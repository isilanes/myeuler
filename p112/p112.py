#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def isbouncy(num):
        '''
        Returns True if number num is bouncy, False otherwise.
        '''

        increasing = False
        decreasing = False

        d = [ int(x) for x in str(num) ]
        for i in range(len(d)-1):
            if d[i] > d[i+1]:
                decreasing = True
            elif d[i] < d[i+1]:
                increasing = True
            if decreasing or increasing:
                break

        n = i + 2
        if n > len(d):
            return False

        if increasing:
            for i in range(n, len(d)):
                if d[i] < d[i-1]: # then it's bouncy
                    return True
        else:
            for i in range(n, len(d)):
                if d[i] > d[i-1]: # then it's bouncy
                    return True

        return False
    
    bouncys = 0.0
    num = 100
    while True:
        num += 1
        if isbouncy(num):
            bouncys += 1.0
        if bouncys / num >= 0.99:
            print(num)
            break

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 1.6 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
