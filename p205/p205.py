from libeuler import core


def p205(n=None):
    # 6x 6-sided dice:
    count_six = get_count_six()

    # Cumulative 6x 6-sided dice:
    cumulative_six = get_cumulative_six(count_six)

    # 9x 4-sided dice:
    count_four = get_count_four()

    fours_above = 0  # how many times 9x 4-sided dice roll is above 6x 6-sided
    for i, n in enumerate(count_four):
        c = count_six_less_than(cumulative_six, i)
        fours_above += c*n

    return round(fours_above/(4**9 * 6**6), 7)


def get_count_six():
    """6x 6-sided dice."""

    count_six = [0 for _ in range(6 * 6 + 2)]
    for i_first in range(1, 7):
        for i_second in range(1, 7):
            for i_third in range(1, 7):
                for i_fourth in range(1, 7):
                    for i_fifth in range(1, 7):
                        for i_sixth in range(1, 7):
                            r = i_first + i_second + i_third + i_fourth + i_fifth + i_sixth
                            count_six[r] += 1

    return count_six


def get_cumulative_six(count):
    """Cumulative 6x 6-sided dice."""

    cumulative_six = [0 for _ in range(6 * 6 + 2)]
    so_far = 0
    for i, val in enumerate(count):
        cumulative_six[i] = so_far
        so_far += val

    return cumulative_six


def count_six_less_than(cumulative, n):
    """How many occurrences of a 6x 6-sided die-roll being LESS than 'n',
    out of the 6**6 combinations.
    """

    return cumulative[n]


def get_count_four():
    """9x 4-sided dice."""

    count_four = [0 for _ in range(9 * 4 + 2)]
    for i_first in range(1, 5):
        for i_second in range(1, 5):
            for i_third in range(1, 5):
                for i_fourth in range(1, 5):
                    for i_fifth in range(1, 5):
                        for i_sixth in range(1, 5):
                            for i_seventh in range(1, 5):
                                for i_eighth in range(1, 5):
                                    for i_ninth in range(1, 5):
                                        r = i_first + i_second + i_third + i_fourth + i_fifth + i_sixth \
                                            + i_seventh + i_eighth + i_ninth
                                        count_four[r] += 1

    return count_four


if __name__ == "__main__":
    core.run_functions([p205])

# Python 3.7.3 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    -                     f0       62.8
#
# pypy3 7.1.0-beta0 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    -                     f0       23.6
