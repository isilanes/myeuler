# Standard libs:
import sys

# Our libs:
sys.path.append("..")
from libeuler import core


# Functions:
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
    def combi(code):
        code = code[1:]  # chop off first char, which should always be a 1
        for i, c in enumerate(code):
            if c == "1":
                nzeros = i
                ncombos = nzeros + 1
                C = combi(code[i:])
                return ncombos*C + ncombos*(C-1)
        
        nzeros = len(code) - 1
        
        return nzeros + 1
        
    initial = bin(n)[2:]  # remove 'b0' from beginning
    print(n, initial)
    
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

