#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    class WeightedEdge(object):

        def __init__(self, src, dest, weight):
            self.src = src
            self.dest = dest
            self.weight = weight

    class DijkstraNode(object):

        def __init__(self):
            self.node = None
            self.tpath = [] # tentative path
            self.tval = None # tentative value

        def __cmp__(self, other):
            return cmp(self.tval, other.tval)

    class Digraph(object):

        def __init__(self):
            self.nodes = []
            self.edges = {}
            self.min_p = None # minimal path
            self.min_v = 10**6 # value of minimal path

        def add_node(self, node):
            self.nodes.append(node)
            self.edges[node] = []

        def add_edge(self, edge):
            src = edge.src
            self.edges[src].append(edge)

        def Dijkstra(self, initial, final):
            '''
            Use: https://en.wikipedia.org/wiki/Dijkstra's_algorithm
            to travel from initial node to final one.
            '''

            # Initial population of "unvisited" nodes:
            unvisited = {}
            for node,edges in self.edges.items():
                for edge in edges:
                    DN = DijkstraNode()
                    DN.node = edge.dest
                    DN.tval = 1000*1000
                    unvisited[edge.dest] = DN

            # Initial node:
            DN = DijkstraNode()
            DN.node = initial
            DN.tval = 0
            unvisited[initial] = DN

            # Loop over all unvisited, until solution:
            while True:
                # Take "current" node as "cheapest" to reach so far:
                curr = sorted(unvisited.values())[0]

                # If we reached destination, quit:
                if curr.node == final:
                    return curr.tval, curr.tpath

                # Check all neighbours to current:
                for e in self.edges[curr.node]:
                    if e.dest in unvisited:
                        tv = curr.tval + e.weight
                        if tv < unvisited[e.dest].tval:
                            unvisited[e.dest].tval = tv
                            unvisited[e.dest].tpath = curr.tpath + [e.dest]

                # Once all neighbours checked, mark current as visited:
                del unvisited[curr.node]

    # Read vertex values from file:
    vertices = []
    with open("matrix.txt") as f:
        for line in f:
            a = [ int(x) for x in line.split(',') ]
            vertices.append(a)

    # Create digraph and populate nodes and edges:
    G = Digraph()
    N = len(vertices)

    # Fictional "initial" node that leads to all nodes in first column:
    G.add_node("initial")
    for i in range(N):
        e = WeightedEdge("initial", (i,0), vertices[i][0])
        G.add_edge(e)

    # Populate rest of nodes/edges:
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

    # Fictional "final" node lead to from all nodes in last column:
    G.add_node("final")
    for i in range(N):
        e = WeightedEdge((i,N-1), "final", 0)
        G.add_edge(e)

    # Perform search:
    v, p = G.Dijkstra("initial", "final")
    print(v)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 21 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
