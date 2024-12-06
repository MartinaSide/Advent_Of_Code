from collections import defaultdict

from aoc import input_as_lines

inp = input_as_lines("day16.txt")
cave = defaultdict()

for row, line in enumerate(inp):
    for col, c in enumerate(line):
        cave[(col, row)] = c

ROWS = len(inp)
COLS = len(inp[0])

# N, E, S, W
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

angles = {
    ".": {
        (0, -1): [0],
        (0, 1): [0],
        (-1, 0): [0],
        (1, 0): [0],
    },
    "|": {
        (0, -1): [0],
        (0, 1): [0],
        (-1, 0): [-1, 1],
        (1, 0): [-1, 1],
    },
    "-": {
        (0, -1): [-1, 1],
        (0, 1): [-1, 1],
        (-1, 0): [0],
        (1, 0): [0],
    },
    "/": {
        (0, -1): [1],
        (0, 1): [1],
        (-1, 0): [-1],
        (1, 0): [-1],
    },
    "\\": {
        (0, -1): [-1],
        (0, 1): [-1],
        (-1, 0): [1],
        (1, 0): [1],
    },

}


def hash_beam(beam, next_cell):
    return f"{beam[0][0]}_{beam[0][1]}_{beam[1][0]}_{beam[1][1]}_{next_cell[0]}_{next_cell[1]}"


def energize(beams):
    energized = []
    seen = []
    while len(beams) > 0:
        new_beams = []
        finished_beams = []
        for beam in beams:
            cur_dir = beam[1]
            next_col = beam[0][0] + cur_dir[0]
            next_row = beam[0][1] + cur_dir[1]
            next_cell = (next_col, next_row)
            if next_col < 0 or next_col >= COLS or next_row < 0 or next_row >= ROWS or hash_beam(beam,
                                                                                                 next_cell) in seen:
                finished_beams.append(beam)
                continue
            seen.append(hash_beam(beam, next_cell))
            dir_changes = angles[cave[next_cell]][cur_dir]
            beam[0] = next_cell
            beam[1] = dirs[(dirs.index(cur_dir) + dir_changes[0]) % len(dirs)]
            if len(dir_changes) == 2:
                new_beam = []
                new_beam.append(next_cell)
                new_beam.append(dirs[(dirs.index(cur_dir) + dir_changes[1]) % len(dirs)])
                new_beams.append(new_beam)
            if next_cell not in energized:
                energized.append(next_cell)
        beams += new_beams
        for b in finished_beams:
            beams.remove(b)
    return len(energized)


# Part 1
print(energize([[(-1, 0), (1, 0)]]))

# Part 2
max_energy = 0
for row in range(ROWS):
    starting_beam = [(-1, row), (1, 0)]
    max_energy = max(max_energy, energize([starting_beam]))

for row in reversed(range(ROWS)):
    starting_beam = [(ROWS, row), (-1, 0)]
    max_energy = max(max_energy, energize([starting_beam]))

for col in range(COLS):
    starting_beam = [(col, -1), (0, 1)]
    max_energy = max(max_energy, energize([starting_beam]))

for col in reversed(range(COLS)):
    starting_beam = [(col, COLS), (0, -1)]
    max_energy = max(max_energy, energize([starting_beam]))

print(max_energy)