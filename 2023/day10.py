def process_input(file_name):
    """Acquire input data"""
    with open(file_name) as file:
        input_file = file.read().splitlines()

    maze = {}
    width = len(input_file[0])
    heigth = len(input_file)
    start_coordinates = (0, 0)

    for y, line in enumerate(input_file):
        for x, ch in enumerate(line):
            maze[(x, y)] = ch
            if ch == 'S':
                start_coordinates = (x, y)

    return maze, width, heigth, start_coordinates


def find_loop():
    """Find all tiles that are on the loop"""
    global start_tile
    steps = 0
    loop = set()
    current = start
    move = 'S'
    start_tile = determine_start_tile()

    while True:
        loop.add(current)
        current, move = next_tile(current, move)
        steps += 1
        if current == start:
            break
    return loop, steps, start_tile


def next_tile(current, move_dir):
    global start_tile
    cx, cy = current
    from_dir = reverse_dir[move_dir]
    current_tile = maze[current]
    if current == start:
        current_tile = start_tile
    directions = moves[current_tile]
    for move in directions:
        if move != from_dir:
            new_tile, new_pos = tile_at(current, move)
            return new_pos, move
    return ''


def determine_start_tile():
    directions = ''
    for move in ('N', 'E', 'W', 'S'):
        from_dir = reverse_dir[move]
        next_ch, next_pos = tile_at(start, move)
        if from_dir in moves[next_ch]:
            directions += move
    if directions in ('NS', 'SN'):
        first_tile_char = '|'
    elif directions in ('EW', 'WE'):
        first_tile_char = '-'
    elif directions in ('NE', 'EN'):
        first_tile_char = 'L'
    elif directions in ('NW', 'NW'):
        first_tile_char = 'J'
    elif directions in ('SW', 'WS'):
        first_tile_char = '7'
    elif directions in ('SE', 'ES'):
        first_tile_char = 'F'
    return first_tile_char


def tile_at(pos, move):
    x, y = pos
    a, b = tile_adjust[move]
    new_pos = (x + a, y + b)
    if new_pos in maze:
        ch = maze[new_pos]
    else:
        ch = '.'
    return ch, new_pos


def count_enclosed():
    enclosed_areas = 0
    for y in range(y_len):
        for x in range(x_len):
            if (x, y) in loop: continue
            if (loop_tiles_to_edge(x, y) % 2) != 0:
                enclosed_areas += 1
    return enclosed_areas


def loop_tiles_to_edge(x, y):
    """Count how many tiles are between the x,y position and the edge of the maze"""
    loop_tiles = 0
    for a in range(0, x):
        if (a, y) in loop:
            weight = 0
            tile = maze[(a, y)]
            if tile == 'S': tile = start_tile
            if tile == '|':
                weight += 1
            elif tile in ('L', '7'):
                weight += .5
            elif tile in ('J', 'F'):
                weight -= .5
            loop_tiles += weight
    return int(loop_tiles)


# -----------------------------------------------------------------------------------------

filename = 'day10.txt'

maze, x_len, y_len, start = process_input(filename)

moves = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE', '.': ''}
reverse_dir = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
tile_adjust = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}

loop, loop_len, start_tile = find_loop()

furthest = int(loop_len / 2)
print()
print('Part 1:', furthest)

enclosed = count_enclosed()

print('Part 2:', enclosed)
print()
