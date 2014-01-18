#--------------------------------------------------------------------#

def f0():
    '''
    http://en.wikipedia.org/wiki/Prim's_algorithm.
    '''
    print("--- f0 ---")

    class Vertex(object):

        def __init__(self):
            self.i = None
            self.edges = []

    class Edge(object):

        def __init__(self):
            self.w = None
            self.src = None
            self.dest = None

    class Graph(object):

        def __init__(self):
            self.vertices = {}
            self.edges = []
        
    # Read grid info:
    G = Graph()
    with open("network.txt") as f:
        i = 0
        for line in f:
            a = line.strip().split(',')
            for j in range(i+1,len(a)): # only read upper right triangle
                if a[j] != '-':
                    # Add i -> j edge:
                    E = Edge()
                    E.w = int(a[j])
                    E.src = i
                    E.dest = j
                    G.edges.append(E)

                    # Add vertex i:
                    if not i in G.vertices:
                        V = Vertex()
                        V.i = i
                        G.vertices[i] = V
                    G.vertices[i].edges.append(E)

                    # Add j -> i edge:
                    E = Edge()
                    E.w = int(a[j])
                    E.src = j
                    E.dest = i
                    G.edges.append(E)

                    # Add vertex j:
                    if not j in G.vertices:
                        V = Vertex()
                        V.i = j
                        G.vertices[j] = V
                    G.vertices[j].edges.append(E)
            i += 1

    # Initial sum:
    s0 = 0
    for e in G.edges:
        s0 += e.w
    s0 = s0/2 # avoid duplication

    # Prim's algorithm:
    Vnew = [0] # selected vertices, pick first at "random"
    Enew = [] # selected edges
    while len(Vnew) < len(G.vertices):
        # Pick all edges coming out of vertices already in Vnew,
        # but pointing to a vertex still out of Vnew:
        outwards = None
        min_val = 9999
        for i in Vnew:
            v = G.vertices[i]
            for e in v.edges:
                if not e.dest in Vnew:
                    if e.w < min_val:
                        outwards = e
                        min_val = e.w

        # Add chosen edge to list of edges (Enew), and chosen vertex
        # to list of vertices (Vnew):
        Vnew.append(outwards.dest)
        Enew.append(outwards)

    # Final sum:
    tot = 0
    for e in Enew:
        tot += e.w

    # "Saved":
    print(s0 - tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 9.4 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
