def f0():
    print("--- f0 ---")

    class WeightedEdge(object):

        def __init__(self, src, dest, weight):
            self.src = src
            self.dest = dest
            self.weight = weight

    class Digraph(object):

        def __init__(self):
            self.nodes = []
            self.edges = {}
            self.final = (None, None)
            self.cache = {} # for memoized DFS

        def add_node(self, node):
            self.nodes.append(node)
            self.edges[node] = []

        def add_edge(self, edge):
            src = edge.src
            self.edges[src].append(edge)

        def DFS(self, node=(0,0)):
            """Return cheapest path from node to self.final."""

            if node == self.final:
                return 0, []
            
            if node in self.cache:
                return self.cache[node]
            
            # Minimum values so far:
            min_value = 1000000
            min_path = None

            for e in self.edges[node]:
                v, p = self.DFS(e.dest)
                v += e.weight
                if v < min_value:
                    min_value = v
                    min_path = [e.dest] + p

            self.cache[node] = min_value, min_path

            return min_value, min_path


    # Read vertex values from file:
    vertices = []
    with open("matrix.txt") as f:
        for line in f:
            a = [ int(x) for x in line.split(',') ]
            vertices.append(a)

    # Create digraph and populate nodes and edges:
    G = Digraph()
    N = len(vertices)

    # Fictional "initial" node that only leads to (0,0):
    G.add_node((N,N))
    e = WeightedEdge((N,N), (0,0), vertices[0][0])
    G.add_edge(e)

    # Final destination node:
    G.final = (N-1, N-1)

    # Populate rest of nodes:
    for i in range(N):
        for j in range(N):
            # Add node:
            src = (i,j)
            G.add_node(src)

            # Add rightwards edge:
            dest = (i,j+1)
            try:
                w = vertices[i][j+1]
                e = WeightedEdge(src, dest, w)
                G.add_edge(e)
            except:
                pass
            
            # Add downwards edge:
            dest = (i+1,j)
            try:
                w = vertices[i+1][j]
                e = WeightedEdge(src, dest, w)
                G.add_edge(e)
            except:
                pass

    # Do a DFS:
    v, p = G.DFS((N,N))
    print(v)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 74 ms
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
