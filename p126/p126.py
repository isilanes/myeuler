#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def nlayer(A,B,C,nmax):
        '''
        Returns an array of [n1,n2,n3...nj], where ni is the amount of
        cubes to fill i-th layer on a AxBxC cuboid. The list of layers
        goes one until layer j, where nj first exceeds nmax.
        '''

        if not A % 2:
            A = A / 2
            dirsA = [(1,0,0)]
            nmulA = 2
        else:
            dirsA = [(1,0,0), (-1,0,0)]
            nmulA = 1

        if not B % 2:
            B = B / 2
            dirsB = [(0,1,0)]
            nmulB = 2
        else:
            dirsB = [(0,1,0), (0,-1,0)]
            nmulB = 1

        if not C % 2:
            C = C / 2
            dirsC = [(0,0,1)]
            nmulC = 2
        else:
            dirsC = [(0,0,1), (0,0,-1)]
            nmulC = 1

        dirs = dirsA + dirsB + dirsC
        nmul = nmulA * nmulB * nmulC

        # A dict with (x,y,z) -> True, where (x,y,z) are positions
        # in space that are filled:
        occu = {}
        tmp = {} # tmp copy of occu. tmp varies, occu is fixed:

        # Initial fill of occu:
        for i in range(A):
            for j in range(B):
                for k in range(C):
                    occu[(i,j,k)] = True
                    tmp[(i,j,k)] = True

        # Fill adjacents to ABC, and count them (only once!):
        res = []
        ind = 0

        while True:
            res.append(0)
            for i,j,k in occu:
                # Six directions around:
                #for adj in [(i+1,j,k), (i-1,j,k), (i,j+1,k), (i,j-1,k), (i,j,k+1), (i,j,k-1)]:
                for dir in dirs:
                    adj = (i+dir[0], j+dir[1], k+dir[2])
                    if not adj in tmp:
                        tmp[adj] = True
                        res[ind] += nmul
            for e in tmp:
                occu[e] = True

            ind += 1
            if res[-1] > nmax:
                break

        return res

    # Maximum cubes per single layer:
    nmax = 500

    # Max dimension for A:
    Amax = nmax / 4

    # Dict with n -> a, where a is amount of layers in various AxBxC
    # cuboids to have exactly n cubes.
    cub = {}
    
    for A in range(1,Amax+1):
        for B in range(1,A+1):
            if 2*A*B + 2*(A+B) > nmax:
                break
            for C in range(1,B+1):
                if 2*A*B + 2*A*C + 2*B*C > nmax:
                    break
                nl = nlayer(A,B,C,nmax)
                for e in nl:
                    try:
                        cub[e] += 1
                    except:
                        cub[e] = 1

    print cub[22]
    print cub[46]
    print cub[78]
    print cub[118]

    for i in sorted(cub.keys()):
        if i in cub:
            if cub[i] == 100:
                print ">", i
            elif cub[i] == 1000:
                print ">>", i
                break

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    def nlayersAB(A,B,n):
        '''
        '''

        res = [A*B]
        prev = A*B
        for layer in range(2,n+1):
            v = prev + A + B + layer - 2
            res.append(v)
            prev = v

        return res

    def nlayers(A,B,C,n):
        '''
        '''

        res = []
        for i,j,k in zip(nlayersAB(A,B,n),nlayersAB(A,C,n),nlayersAB(B,C,n)):
            res.append((i+j+k)*2)

        return res

    print nlayers(3,2,1,4)
    print nlayers(5,1,1,1)
    print nlayers(5,3,1,1)
    print nlayers(7,2,1,1)
    print nlayers(11,1,1,1)

#--------------------------------------------------------------------#

def f2():
    print("--- f2 ---")

    def nlayers(A,B,C,n):
        '''
        '''

        # Face AB:
        nAB = [A*B]
        for ilayer in range(1,n):
            ni = nAB[-1] + (A + B) + 4*(ilayer-1)
            nAB.append(ni)

        # Face AC:
        nAC = [A*C,0,0]

        # Face BC:
        nBC = [B*C,0,0]

        res = []
        for i,j,k in zip(nAB,nAC,nBC):
            v = 2*(i+j+k)
            res.append(v)

        return res

    print nlayers(3,2,1,4)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2,3):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: too slow
# f1:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
