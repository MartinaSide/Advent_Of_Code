from copy import deepcopy

from aoc import input_as_lines, print_matrix

inp = input_as_lines("day14.txt")
N = []

for line in inp:
    N.append([r for r in line])

ROWS = len(N)
COLS = len(N[0])

def tilt(N):
    ROWS = len(N)
    COLS = len(N[0])
    top_blocks = [0] * COLS
    for row in range(ROWS):
        for col in range(COLS):
            cell = N[row][col]
            if cell == "#":
                top_blocks[col] = row + 1
            if cell == "O":
                top_blocks[col] += 1
                N[row][col] = "."
                N[top_blocks[col] - 1][col] = "O"

def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)
    return new_matrix

def calc_load(N):
    s1 = 0
    for row in range(ROWS):
        val = ROWS - row
        s1 += val * N[row].count("O")
    return s1

def part1():
    tilt(N)
    return calc_load(N)

def part2():
    global N
    N = rotate_90_degree_clckwise(N)
    tilt(N)
    N = rotate_90_degree_clckwise(N)
    tilt(N)
    N = rotate_90_degree_clckwise(N)
    tilt(N)
    N = rotate_90_degree_clckwise(N)
    matrixes = [deepcopy(N)]
    for cycle in range(1, 999999999):
        for _ in range(4):
            tilt(N)
            N = rotate_90_degree_clckwise(N)
        if N not in matrixes:
            matrixes.append(deepcopy(N))
            continue
        ind = matrixes.index(N)
        cycle_length = cycle - ind
        remaining = 999999999 - cycle
        offset = remaining % cycle_length
        return calc_load(matrixes[ind + offset])
    return calc_load(N)


print(part1())
print(part2())
