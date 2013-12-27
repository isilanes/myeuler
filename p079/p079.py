#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def can_has(arr, n):
        '''
        arr is an array of digits. can_has returns True if 3-digit 
        string n can be build by picking 3 ordered digits from arr,
        False otherwise.
        '''

        try:
            i = arr.index(n[0])
        except ValueError:
            return False
        arr = arr[i+1:]

        try:
            j = arr.index(n[1])
        except ValueError:
            return False
        arr = arr[j+1:]

        if not n[2] in arr:
            return False

        return True

    def has_all(arr, numbers):
        '''
        Returns True if can_has(arr, x) is True for every x in numbers,
        False otherwise.
        '''

        for number in numbers:
            if not can_has(arr, number):
                return False

        return True

    # Read input into array:
    numbers = []
    with open("keylog.txt") as f:
        for line in f:
            n = line.strip()
            numbers.append(n)

    i = 9999999
    while True:
        s = str(i)
        if has_all(s, numbers):
            print(s)
            break
        else:
            i += 1

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
