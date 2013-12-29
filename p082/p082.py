#--------------------------------------------------------------------#

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
            self.final = None
            self.cache = {} # for memoized DFS
            self.min_p = None # minimal path
            self.min_v = 10**6 # value of minimal path

        def add_node(self, node):
            self.nodes.append(node)
            self.edges[node] = []

        def add_edge(self, edge):
            src = edge.src
            self.edges[src].append(edge)

        def DFS(self, path, value):
            '''
            Return cheapest path from node to self.final.
            "path" is the path so far (the node list). We use
            the whole path, and not just the last node (as in
            p081), because we need to avoid loops in the paths.
            "value" is the value of path so far.
            '''

            # Last node in path:
            node = path[-1]

            # If we arrived to the destination:
            if node[1] == self.final:
                if value < self.min_v:
                    self.min_v = value
                    self.min_p = path
                    print path, self.min_v
                return [], 0

            # If cached:
            #if node in self.cache:
            #    print node, self.cache[node]
            #    return self.cache[node]

            # Minimum values so far:
            min_value = 1000000
            min_path = None

            for e in self.edges[node]:
                if not e.dest in path: # avoid loops
                    np = path + [e.dest]
                    nv = value + e.weight
                    p, v = self.DFS(np, nv)
                    v += e.weight
                    if v < min_value:
                        min_value = v
                        min_path = [e.dest] + p

            self.cache[node] = min_path, min_value
            return min_path, min_value

    # Read vertex values from file:
    vertices = []
    with open("minimatrix.txt") as f:
        for line in f:
            a = [ int(x) for x in line.split(',') ]
            vertices.append(a)

    # For debugging:
    #vertices = [ line[:9] for line in vertices[:9] ]

    # Create digraph and populate nodes and edges:
    G = Digraph()
    N = len(vertices)

    # Fictional "initial" node that leads to all nodes in
    # first column:
    G.add_node("initial")
    for i in range(N):
        e = WeightedEdge("initial", (i,0), vertices[i][0])
        G.add_edge(e)

    # Final destination column:
    G.final = N-1

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
            if i + 1 < N:
                dest = (i+1,j)
                w = vertices[i+1][j]
                e = WeightedEdge(src, dest, w)
                G.add_edge(e)

            # Add upwards edge:
            if i > 0:
                dest = (i-1,j)
                w = vertices[i-1][j]
                e = WeightedEdge(src, dest, w)
                G.add_edge(e)

    # For debugging:
    #for e in G.edges[(1,2)]: print e.dest

    # Do a DFS:
    G.DFS(["initial"], 0)
    print G.min_v, G.min_p

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
