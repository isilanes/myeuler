from libeuler import core


def f0(n=None):
    
    def children_of(parent):
        children = []
        for i, char in enumerate(parent[:-1]):  # ignore last value (already 2^0)
            if char == "1" and parent[i+1] == "0":  # xxx10xxx -> xxx02xxx
                new = parent[:i] + "02" + parent[i+2:]
                children.append(new)
            elif char == "2" and parent[i+1] == "0":  # xxx20xxx -> xxx12xxx
                new = parent[:i] + "12" + parent[i+2:]
                children.append(new)
            
        return children
    
    # Initialize:
    initial = bin(n)
    valids = [initial]
    potential = children_of(initial)
    valids.extend(potential)

    # Loop:
    while potential:
        new_potential = []
        for case in potential:
            for child in children_of(case):
                if child not in valids:
                    new_potential.append(child)
                    valids.append(child)
        
        potential = new_potential
    
    return len(valids)


def f1(n=None):
    
    def children_of(parent):
        children = []
        for i, char in enumerate(parent[:-1]):  # ignore last value (already 2^0)
            if parent[i+1] == "0":
                if char == "1":  # xxx10xxx -> xxx02xxx
                    new = parent[:i] + "02" + parent[i+2:]
                    children.append(new)
                elif char == "2":  # xxx20xxx -> xxx12xxx
                    new = parent[:i] + "12" + parent[i+2:]
                    children.append(new)
        
        return children
    
    # Initialize:
    initial = bin(n)
    valids = {
        initial: True,
    }
    potential = children_of(initial)
    for case in potential:
        valids[case] = True
    
    # Loop:
    while potential:
        new_potential = []
        for case in potential:
            for child in children_of(case):
                if child not in valids:
                    new_potential.append(child)
                    valids[child] = True
        
        potential = new_potential
    
    return len(valids)


def f2(n):
    def combi(code, pre_combis=None):
        i = code.rfind("1")
        chopped = code[:i]
        n_zeros = len(code) - i - 1
        
        if pre_combis is None:
            if not chopped:
                return n_zeros + 1
            
            return combi(chopped, (n_zeros, 1))
        
        k_zero = n_zeros * sum(pre_combis) + pre_combis[0]
        k_one = sum(pre_combis)
        
        if not chopped:
            return k_zero + k_one
        
        return combi(chopped, (k_zero, k_one))
        
    initial = bin(n)[2:]  # remove 'b0' from beginning
    
    return combi(initial)
    
    
# Main code:
if __name__ == "__main__":
    core.run_functions([f0, f1, f2])

# PyPy 5.10.0 times (Manjaro)
#
#         n              res(n)  function  time (ms)
#        10                   5        f0        0.1
#       100                  19        f0        0.3
#      1000                  39        f0        0.7
#     10000                 205        f0       11.7
#     10**6                1287        f0       41.1
#     10**8                7901        f0      611.2
#    10**10               77695        f0    66200
#
#         n              res(n)  function  time (ms)
#        10                   5        f1        0.2
#       100                  19        f1        0.4
#      1000                  39        f1        0.6
#     10000                 205        f1        6.2
#     10**6                1287        f1       24.8
#     10**8                7901        f1       32.7
#    10**10               77695        f1      123.1
#    10**12             2077157        f1     5600
#    10**14             5946265        f1    18500
#    10**16            17165857        f1    62400
#
#         n              res(n)  function  time (ms)
#        10                   5        f2        0.1
#       100                  19        f2        0.1
#      1000                  39        f2        0.1
#     10000                 205        f2        0.1
#     10**6                1287        f2        0.2
#     10**8                7901        f2        0.2
#    10**10               77695        f2        0.2
#    10**12             2077157        f2        0.2
#    10**14             5946265        f2        0.7
#    10**16            17165857        f2        0.2
#    10**18           554817437        f2        0.3
#    10**20          5483345119        f2        0.3
#    10**25        178653872807        f2        0.4

