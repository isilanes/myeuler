#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def best_sum(N):
        elements = [N]
        for j in range(30):
            if not N % 2:
                elements.append(N/2)
                N = N / 2
            else:
                i = N // 2
                while True:
                    if not (N-i) % i:
                        break
                    i -= 1
                elements.append(N-i)
                elements.append(i)
                N = N - i
            print elements, N
            if N < 3:
                break

        elements = list(set(elements))
        if 1 in elements:
            elements.remove(1)
        return sorted(elements)

    print best_sum(65)
    return
    tot = 0
    for k in range(2,201):
        tot += len(best_sum(k))
        print k, best_sum(k)

    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 10 ms (python3)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
