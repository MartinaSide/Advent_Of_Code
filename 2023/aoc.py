# aoc.py
import os
import re
from typing import List


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def input_as_lines(filename: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def input_as_ints(filename: str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)

    def line_as_int(l): return int(l.rstrip('\n'))

    return list(map(line_as_int, lines))


def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(x) for x in row]))
    print()


def print_matrix_reverse(matrix):
    for row in matrix[::-1]:
        print(" ".join([str(x) for x in row]))


def flatten(l):
    return [item for sublist in l for item in sublist]


def print_dict_as_matrix(d):
    """
    Helper to convert a dict cave to a matrix and print it
    """
    min_col = 2 ** 10000
    max_col = -2 ** 10000
    min_row = 2 ** 10000
    max_row = -2 ** 10000
    for point in d.keys():
        col, row = point
        min_col = min(col, min_col)
        max_col = max(col, max_col)
        min_row = min(row, min_row)
        max_row = max(row, max_row)
    COLS = max_col - min_col + 1
    ROWS = max_row - min_row + 1
    cave = [["." for col in range(COLS)] for row in range(ROWS)]
    for point in d.keys():
        col, row = point
        cave[row - min_row][col - min_col] = d[point]
    print("\n")
    print_matrix(cave)


def parse_ints_str(line: str) -> List[int]:
    return [int(x) for x in re.findall(r'[\+\-]?[0-9]+', line)]


def parse_positive_ints_str(line: str) -> List[int]:
    return [int(x) for x in re.findall(r'[\+]?[0-9]+', line)]


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def generate_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    days = [int(re.findall(r'\d+', f)[0])
            for f in files if f.startswith("day")]
    next_day = max(days) + 1
    next_day_str = str(next_day)
    open("day" + next_day_str + ".py", "w").close()
    open("day" + next_day_str + ".txt", "w").close()
    open("day" + next_day_str + "t.txt", "w").close()
    print("Created day" + next_day_str + "files.")


def get_manhattan_distance(p, q):
    """
    Return the manhattan distance between points p and q
    assuming both to have the same number of dimensions
    """
    distance = 0
    for p_i, q_i in zip(p, q):
        distance += abs(p_i - q_i)
    return distance


if __name__ == "__main__":
    generate_files()
