#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math

    thres = 10**-6

    nin = 0
    with open("triangles.txt") as f:
        for line in f:
            a = [ float(x) for x in line.split(",") ]
            A = a[:2]
            B = a[2:4]
            C = a[4:]

            # A-O-B angle:
            p = A[0]*B[0] + A[1]*B[1]
            rA = math.sqrt(A[0]**2 + A[1]**2)
            rB = math.sqrt(B[0]**2 + B[1]**2)
            cosAOB = p/(rA*rB)
            AOB = math.acos(cosAOB)

            # B-O-C angle:
            p = B[0]*C[0] + B[1]*C[1]
            rC = math.sqrt(C[0]**2 + C[1]**2)
            cosBOC = p/(rB*rC)
            BOC = math.acos(cosBOC)

            # C-O-A angle:
            p = C[0]*A[0] + C[1]*A[1]
            cosCOA = p/(rC*rA)
            COA = math.acos(cosCOA)

            s = AOB + BOC + COA
            e = abs(s - 2*math.pi)
            if e < thres:
                nin += 1

    print(nin)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 8.5 ms
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
