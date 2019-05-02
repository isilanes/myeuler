# Standard libs:
import sys

# Our libs:
sys.path.append("..")
from libeuler import core


# Globals:


# Functions:
def p205(n=None):
    # 6x 6-sided dice:
    count_six = [0 for _ in range(6 * 4 + 1)]
    for i_first in range(1, 7):
        for i_second in range(1, 7):
            for i_third in range(1, 7):
                for i_fourth in range(1, 7):
                    r = i_first + i_second + i_third + i_fourth
                    count_six[r] += 1
    
    print(count_six)
    
    # Cumulative 6x 6-sided dice:
    cumulative_six = [0 for _ in range(6 * 4 + 1)]
    so_far = 0
    for i, val in enumerate(count_six):
        cumulative_six[i] = so_far
        so_far += val
    print(cumulative_six)
    
    # Prob n+:
    print(n, 1.0 - cumulative_six[n]/sum(count_six))


# Main code:
if __name__ == "__main__":
    core.run_functions([p205])

# Python 3.7.3 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    -

