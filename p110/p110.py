#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def get_n(plist,some_elist):
        n = 1
        for i in range(len(some_elist)):
            n = n * plist[i]**some_elist[i]
        return n

    plist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    nmin = 41856930490307832900
    for e1 in range(4):
      for e2 in range(4):
        for e3 in range(4):
          for e4 in range(4):
            elist = [e1,e2,e3,e4]
            if get_n(plist, elist) > nmin:
                break
            for e5 in range(4):
              elist = [e1,e2,e3,e4,e5]
              if get_n(plist, elist) > nmin:
                  break
              for e6 in range(4):
                elist = [e1,e2,e3,e4,e5,e6]
                if get_n(plist, elist) > nmin:
                    break
                for e7 in range(4):
                  elist = [e1,e2,e3,e4,e5,e6,e7]
                  if get_n(plist, elist) > nmin:
                      break
                  for e8 in range(4):
                    elist = [e1,e2,e3,e4,e5,e6,e7,e8]
                    if get_n(plist, elist) > nmin:
                        break
                    for e9 in range(4):
                      elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9]
                      if get_n(plist, elist) > nmin:
                          break
                      for e10 in range(4):
                        elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
                        if get_n(plist, elist) > nmin:
                            break
                        for e11 in range(4):
                          elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11]
                          if get_n(plist, elist) > nmin:
                              break
                          for e12 in range(4):
                            elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
                            if get_n(plist, elist) > nmin:
                                break
                            for e13 in range(4):
                              elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13]
                              if get_n(plist, elist) > nmin:
                                  break
                              for e14 in range(4):
                                elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]
                                if get_n(plist, elist) > nmin:
                                    break
                                for e15 in range(4):
                                  elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15]
                                  d = 1
                                  n = 1
                                  for i in range(len(elist)):
                                      d = d * (2*elist[i]+1)
                                      n = n*plist[i]**elist[i]

                                  d2 = (d+1)/2
                                  if d2 > 4000*1000:
                                      if n < nmin:
                                          print '{0:8d} {1}'.format(d2, n)
                                          nmin = n

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    plist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    nmin = 2*3*5*7*11*13*17*19*23*29*31*37*41*43*47
    for e1 in range(4):
      for e2 in range(e1+1):
        for e3 in range(e2+1):
          for e4 in range(e3+1):
            for e5 in range(e4+1):
              for e6 in range(e5+1):
                for e7 in range(e6+1):
                  for e8 in range(e7+1):
                    for e9 in range(e8+1):
                      for e10 in range(e9+1):
                        for e11 in range(e10+1):
                          for e12 in range(e11+1):
                            for e13 in range(e12+1):
                              for e14 in range(e13+1):
                                  elist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]
                                  d = 1
                                  n = 1
                                  for i in range(len(elist)):
                                      d = d * (2*elist[i]+1)
                                      n = n*plist[i]**elist[i]

                                  d2 = (d+1)/2
                                  if d2 > 4000*1000:
                                      if n < nmin:
                                          print '{0:8d} {1}'.format(d2, n)
                                          nmin = n

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1,2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: slow, but works (~ 120 s, pypy)
# f1: ~ 5 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
