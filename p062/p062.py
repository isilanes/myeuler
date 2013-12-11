#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    digimon = {}

    i = 405
    while True:
        cube = i**3
        digicube = [ x for x in str(cube) ]
        digicube.sort()
        digicube = ''.join(digicube)
        if digicube in digimon:
            digimon[digicube].append(i)
            if len(digimon[digicube]) > 4:
                print(digimon[digicube])
                print(digimon[digicube][0]**3)
                return
        else:
            digimon[digicube] = [i]

        i += 1

#--------------------------------------------------------------------#

def f2():
    '''
    Similar to f1(), posted by tharrison on:
    projecteuler.net/thread=62;page=9
    '''
    print("--- f2 ---")

    class CubeContainer:
        cubeCount = 1
        smallestNum = 1
        smallestCube = 1

    cubes = {}
    numToTest = 1
    GOAL = 5
    while True:
        currentCube = numToTest**3

        currentCube = ''.join(sorted(str(currentCube)))

        if (currentCube in cubes):
            cubes[currentCube].cubeCount += 1
        else:
            cubes[currentCube] = CubeContainer()
            cubes[currentCube].smallestNum = numToTest
            cubes[currentCube].smallestCube = numToTest ** 3

        if (cubes[currentCube].cubeCount == GOAL):
            print ("Cube %d (%d) produced %d cubes" % (cubes[currentCube].smallestNum, cubes[currentCube].smallestCube, GOAL))
            break

        numToTest += 1

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)
t = timeit.Timer('f2()', "from __main__ import f2")
t2 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # 28 ms
print('t2 = {0:.1f} ms'.format(t2*1000)) # 39 ms
