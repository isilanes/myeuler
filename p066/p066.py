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
        '''
        Return True if num is a perfect square.
        '''

        if int(math.sqrt(num))**2 == num:
            return True

        return False

    max_min_x = 0
    for D in range(2,542):

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

import timeit

times = []
for i in range(3):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0() can only compute up to D = 53 in reasonable time
# f1() can only compute up to D = 61 in reasonable time
# f2(), even using Bhaskara's method, D = 541 max reasonable (even 661)
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
