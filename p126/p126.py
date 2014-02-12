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
    nmax = 2000

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
                    if cub[e] > 999:
                        print e, cub[e]
    print cub[22]  # 2
    print cub[46]  # 4
    print cub[78]  # 5
    print cub[118] # 8

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
        
        v0 = 2*A*B + 2*A*C + 2*B*C

        res = []
        for i in range(n):
            v = v0 + 4*i*(A+B+C) + 8*(i-1)*0
            res.append(v)

        return res

    print nlayers(3,2,1,4)  # 22, 46, 78, 118
    print nlayers(5,1,1,1)  # 22
    print nlayers(5,3,1,1)  # 46
    print nlayers(7,2,1,1)  # 46
    print nlayers(11,1,1,1) # 46

#--------------------------------------------------------------------#

def f3():
    print("--- f3 ---")

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

        to_test = occu.keys()[:]
        while True:
            new = []
            res.append(0)
            for i,j,k in to_test:
                for dir in dirs:
                    adj = (i+dir[0], j+dir[1], k+dir[2])
                    if not adj in occu:
                        occu[adj] = True
                        res[ind] += nmul
                        new.append(adj)

            to_test = new[:]
            
            ind += 1
            if res[-1] > nmax:
                break

        return res

    # Maximum cubes per single layer:
    nmax = 7000

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
                    if cub[e] > 999:
                        print e, cub[e]

    print cub[22]  # 2
    print cub[46]  # 4
    print cub[78]  # 5
    print cub[118] # 8
    print nlayer(3,2,1,4)  # 22, 46, 78, 118
    print nlayer(5,1,1,1)  # 22
    print nlayer(5,3,1,1)  # 46
    print nlayer(7,2,1,1)  # 46
    print nlayer(11,1,1,1) # 46

    for i in sorted(cub.keys()):
        if i in cub:
            if cub[i] == 100:
                print ">", i
            elif cub[i] == 1000:
                print ">>", i
                break

#--------------------------------------------------------------------#

def f4():
    '''
    Adapted from: http://glisicv.wordpress.com/2013/01/07/cuboid-layers-p126/
    '''
    print("--- f4 ---")

    from collections import defaultdict

    def calculate_layer(x,y,z,L):   
        return 2*(2*(L-1)*(x+z)+2*(L-1)*(L+y-2)+x*y+x*z+y*z)

    dict1 = defaultdict(int)

    max_v = 20000

    for L in range(1,100):
        for x in range(1,5000):
            if calculate_layer(x,x,x,L) > max_v:
                break

            for y in range(x,5000):
                if calculate_layer(x,y,y,L) > max_v:
                    break
                for z in range(y,5000):
                    if calculate_layer(x,y,z,L) > max_v:
                        break

                    dict1[calculate_layer(x,y,z,L)] += 1

    for x,y in dict1.iteritems():
        if y == 1000:
            print(x)
            break

#--------------------------------------------------------------------#

def f5():
    '''
    Adapted from: http://glisicv.wordpress.com/2013/01/07/cuboid-layers-p126/
    '''
    print("--- f5 ---")

    def perlayer(A,B,C,nmax):
        '''
        Return list [n1,n2... nj], where ni is amount of cuboids in
        i-th layer, and nj is first value over nmax.
        '''
        v0 = 2*(A*B + A*C + B*C)
        res = [v0]
        L = 2
        while True:
            v = 4*(L-1)*(A+C) + 4*(L-1)*(L+B-2) + v0
            res.append(v)
            if v > nmax:
                return res
            L += 1

    # Tests:
    #print perlayer(3,2,1,200)  # 22, 46, 78, 118
    #print perlayer(5,1,1,100)  # 22
    #print perlayer(5,3,1,100)  # 46
    #print perlayer(7,2,1,100)  # 46
    #print perlayer(11,1,1,100) # 46

    nmax = 20000

    cn = {}
    for A in range(1,nmax/4):
        for B in range(1,A+1):
            if 2*A*B + 2*A + 2 > nmax:
                break
            for C in range(1,B+1):
                if 2*(A*B+A*C+B*C) > nmax:
                    break

                for n in perlayer(A,B,C,nmax):
                    try:
                        cn[n] += 1
                    except:
                        cn[n] = 1

    for n,v in cn.items():
        if v == 1000:
            print(n)
            break

#--------------------------------------------------------------------#

import timeit

times = []
for i in [4,5]:
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0-f3: too slow or wrong
# f4: ~ 0.35 s (pypy)
# f5: ~ 0.54 s (pypy, but faster than f4 with python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
