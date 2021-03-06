'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

#-------------------------------------------------------------------------#

def f1(triangle):
    '''Brute force.'''

    max = 0
    combo = [ 0 for x in range(len(triangle)) ]
    max_combo = None
    while combo:
        sum = 0
        for i in range(len(triangle)):
            sum += triangle[i][combo[i]]
            
        if sum > max:
            max = sum
            max_combo = combo[:]

        combo = next(combo)

    return [max_combo, max]

#-------------------------------------------------------------------------#

def f2(triangle):

    l = len(triangle)

    max = triangle[:] # clone a triangle with equal shape

    for i in range(len(triangle[-1])):
        #max[-1][i] = [ triangle[-1][i], [triangle[-1][i]] ]
        max[-1][i] = triangle[-1][i]
    
    for i in range(l-2,-1,-1):
        for j in range(len(triangle[i])):
            # "a" will end up with biggest number among two below current:
            [ a, b ] = triangle[i+1][j:j+2]
            if b > a:
                a = b

            max[i][j] = triangle[i][j] + a

    return max[0][0]

#-------------------------------------------------------------------------#

def next(combo):
    l = len(combo)

    for i in range(l):
        li = l - i - 1
        l2 = li - 1
        if combo[li] == combo[l2]:
            combo[li] += 1
            for j in range(li+2,l):
                combo[j] = combo[li]
            return combo

    return False

#-------------------------------------------------------------------------#

triangle_string = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

triangle = []
i = 0
for line in triangle_string.split('\n'):
    triangle.append([])
    triangle[i] = [ int(x) for x in line.split() ]
    i += 1

res = f2(triangle)

print(res)
