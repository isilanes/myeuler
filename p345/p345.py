import math
import numpy as np
from functools import lru_cache

from libeuler import core


INPUT = {
    5: """  7  53 183 439 863
          497 383 563  79 973
          287  63 343 169 583
          627 343 773 959 943
          767 473 103 699 303""",
    7: """  7  53 183 439 863 497 383
          627 343 773 959 943 767 473
          447 283 463  29  23 487 463
          217 623   3 399 853 407 103
          960 376 682 962 300 780 486
          870 456 192 162 593 473 915
          973 965 905 919 133 673 665""",
    10: """  7  53 183 439 863 497 383 563  79 973
           627 343 773 959 943 767 473 103 699 303
           447 283 463  29  23 487 463 993 119 883
           217 623   3 399 853 407 103 983  89 463
           960 376 682 962 300 780 486 502 912 800
           870 456 192 162 593 473 915  45 989 873
           973 965 905 919 133 673 665 235 509 613
           322 148 972 962 286 255 941 541 265 323
           445 721  11 525 473  65 511 164 138 672
           414 456 310 312 798 104 566 520 302 248""",
    15: """  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
           627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
           447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
           217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
           960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
           870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
           973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
           322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
           445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
           414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
           184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
           821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
            34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
           815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
           813 883 451 509 615  77 281 613 459 205 380 274 302  35 805""",
}
MATRIX = None


def p345(n=None):
    global MATRIX
    
    if n not in INPUT:
        raise Exception("Wrong N.")
    
    MATRIX = input2matrix(INPUT[n])
    
    return matrix_sum_of("")
    

def input2matrix(input_string):
    array = [int(x) for x in input_string.split()]
    d = int(math.sqrt(len(array)))
    
    return np.array(array).reshape((d, d))


@lru_cache(maxsize=40000)
def matrix_sum_of(index_string):
    global MATRIX
    
    indices = ()
    if index_string:
        indices = [int(x) for x in index_string.split(",")]
    
    N = len(indices)
    
    # Delete first N columns, and rows corresponding to indices:
    submatrix = np.delete(MATRIX[:, N:], indices, 0)
    
    if len(submatrix) == 1:
        return submatrix[0, 0]
    
    max_value = 0
    for i in range(len(MATRIX)):
        if i not in indices:
            new_indices = sorted([x for x in indices] + [i])  # sort, to allow cache-ing
            new_indices = ",".join([str(x) for x in new_indices])
            total = MATRIX[i, N] + matrix_sum_of(new_indices)
        
            if total > max_value:
                max_value = total
    
    return max_value


if __name__ == "__main__":
    core.run_functions([p345])

# Python 3.7.3 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    5         3315        f0        4.8
#    7         5712        f0      198.7
#   10         8779        f0    13900
#
#    n       res(n)  function  time (ms)
#    5         3315        f1        1.5
#    7         5712        f1        6.2
#   10         8779        f1       58.6
#   15        13938        f1     2700

