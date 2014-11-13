import math
import timeit

#------------------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def rebote(m0, p):
        '''Given impact point p = [x,y], and slope m of incoming beam,
        return slope m1 of outgoing beam.'''
        
        x, y = p
        a = 8*x*y
        b = 16*x**2 - y**2
        
        return (a - m0*b)/(b + a*m0)

    def corte(m1, p):
        '''Given reflection point p = [x,y], and outgoing slope m1,
        return next impact point.'''
        
        x1, y1 = p
        A = y1 - m1*x1
        s = math.sqrt(100*m1**2 + 400. - 4*A**2)
        xm = (-A*m1 - s) / (4+m1**2)
        xp = (-A*m1 + s) / (4+m1**2)

        # Output x will be the one in (xm, xp) that is NOT x1:
        delta = 10**-6
        x = xm
        if abs(xm - x1) < delta:
            x = xp

        y = A + m1*x
        
        return [x, y]

    def within(p):
        '''Return True if p = [x,y] is such that the beam will exit (hole).'''

        x, y = p
        if x <= 0.01 and x >= -0.01:
            if y > 0:
                return True
        return False


    # Initial beam:
    p = [ 1.4, -9.6 ]
    m = (-9.6 - 10.1) / (1.4 - 0.0)

    nbeams = 1
    while True:
        m = rebote(m, p)
        p = corte(m, p)
        if within(p):
            break
        nbeams += 1

    print(nbeams)


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0: 3.4 ms

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
