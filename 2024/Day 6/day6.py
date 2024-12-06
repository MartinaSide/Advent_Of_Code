def get_coordinates(playing_map, character):
    coordinates = []
    for i in range(len(playing_map)):
        for j in range(len(playing_map[i])):
            if playing_map[i][j] == character:
                coordinates.append((i,j))
    return coordinates


def move(coordinates, map, direction):
    max_x = len(map[0])
    max_y = len(map)
    number_of_moves = 0
    i, j = coordinates
    while True:
        match direction:
            case 'UP':
                look_ahead = i - 1
                if look_ahead < 0:
                    return number_of_moves
                elif map[look_ahead][j] == "#":
                    direction = "RIGHT"
                elif map[look_ahead][j] == ".":
                    i -= 1
                    number_of_moves += 1
                else:
                    i-=1
            case 'DOWN':
                look_ahead = i + 1
                if look_ahead >= max_y:
                    return number_of_moves
                elif map[look_ahead][j] == "#":
                    direction = "LEFT"
                elif map[look_ahead][j] == ".":
                    i += 1
                    number_of_moves += 1
                else:
                    i+=1
            case 'LEFT':
                look_ahead = j - 1
                if look_ahead < 0:
                    return number_of_moves
                elif map[i][look_ahead] == "#":
                    direction = "UP"
                elif map[i][look_ahead] == ".":
                    j -= 1
                    number_of_moves += 1
                else:
                    j-=1
            case 'RIGHT':
                look_ahead = j + 1
                if look_ahead >= max_x:
                    return number_of_moves
                elif map[i][look_ahead] == "#":
                    direction = "DOWN"
                elif map[i][look_ahead] == ".":
                    j += 1
                    number_of_moves += 1
                else:
                    j+=1


def main():
    with open("2024/Day 6/input.txt") as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    data = [list(x) for x in data]
    guard = get_coordinates(data, "^")[0]
    print(move(guard, data, "UP"))


if __name__ == "__main__":
    main()
