#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math
    
    def is_square(num):
        '''
        Return True if num is a perfect square.
        '''

        if int(math.sqrt(num))**2 == num:
            return True

        return False

    def diophan(D,x):
        '''
        Return True if the D,x combination yields an integer y
        in the x**2 + D*y**2 = 1 Diophantine equation.
        '''
        
        if not (x**2 - 1) % D: # then y**2 is integer:
            y2 = (x**2 - 1) / D
            if is_square(y2):
                return True
            
        return False
    
    maxX = 0
    for D in range(2,61):
        if not is_square(D):
            x = 2
            while True:
                if diophan(D,x):
                    if x > maxX:
                        maxX = x
                        print(D,x)
                    break
                x += 1

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    import math
    
    def is_square(num):
        '''
        Return True if num is a perfect square.
        '''

        if int(math.sqrt(num))**2 == num:
            return True

        return False

    def diophan(D,y):
        '''
        Return True if the D,y combination yields an integer x
        in the x**2 + D*y**2 = 1 Diophantine equation.
        '''

        x2 = 1 + D*y**2
        
        if is_square(x2):
            return True
            
        return False
    
    maxX = 0
    for D in range(2,62):
        if not is_square(D):
            y = 2
            while True:
                if diophan(D,y):
                    x = math.sqrt(1 + D*y**2)
                    if x > maxX:
                        maxX = int(x)
                        print(D, maxX, y)
                    break
                y += 1

#--------------------------------------------------------------------#

def f2():
    '''
    See http://en.wikipedia.org/wiki/Pell's_equation
    '''
    print("--- f2 ---")

    import math

    def is_square(num):
        '''Return True if num is a perfect square.'''
        return int(math.sqrt(num))**2 == num

    max_min_x = 0
    for D in range(2,110):

        # Avoid square Ds:
        if is_square(D):
            continue

        # Propose first x,y,k:
        x = D
        y = 1
        k = x**2 - D*y**2

        # Cycle until conditions are met:
        while k != 1:
            m = 1
            # Cycle until correct m is found:
            while True:
                if not (x + m*y) % k:
                    newX = (x*m + D*y) / k
                    newY = (x + m*y) / k
                    newK = (m**2 - D) / k
                    x, y, k = abs(newX), abs(newY), newK
                    break
                m += 1

        # Print result:
        if x > max_min_x:
            max_min_x = x
            print D, (x, y)

#--------------------------------------------------------------------#

def f3():
    '''
    See http://en.wikipedia.org/wiki/Pell's_equation
    '''
    print("--- f3 ---")

    import math

    def is_square(num):
        '''Return True if num is a perfect square.'''
        return int(math.sqrt(num))**2 == num

    def ratio(a0, period, nth):
        
        # Coefficients of convergent:
        coefs = []
        imax = nth / len(period) + 1
        for i in range(imax):
            coefs.extend(period)

        # Initialize loop and proceed:
        A, B = 1, coefs[nth-2]
        for i in range(nth-3,-1,-1):
            A, B = B, B*coefs[i] + A

        # The final numerator and denominator:
        return B*a0 +A, B

    def are_diophantine(D, x, y):
        '''Returns True if Pell's equation is fullfilled. False otherwise.'''
        return x**2 - D*y**2 == 1

    max_x = 0
    for D in range(2,1001):
        # Avoid if perfect square:
        if is_square(D):
            continue

        sD = math.sqrt(D)
        a0 = int(sD)
        A, B = 1, a0
        
        # Find continued-fraction coefficients:
        trios = []
        while True:
            newA = (D - B**2)/A
            newB = a0 - (a0 + B) % newA
            ai = (a0 + B) / newA
            A, B = newA, newB
            trio = [ai, A, B]
            
            if trio in trios: # then we reached periodicity:
                period = [ x[0] for x in trios ]
                break
            else:
                trios.append(trio)

        # Use cont-frac coeffs succesively, until valid num/den
        # couple is found:
        nth = 1
        while True:
            x, y = ratio(a0, period, nth)
            if are_diophantine(D, x, y):
                if x > max_x:
                    max_x = x
                    print D, '->', (x, y)
                break
            nth += 1

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(4):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(), can only compute up to D = 53 in reasonable time
# f1(), can only compute up to D = 61 in reasonable time
# f2(), even using Bhaskara's method, D = 277 reasonable (even up to 661)
# f3(), continued fractions method
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
