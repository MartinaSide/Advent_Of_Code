def find_XMAS(data):
    X = len(data[0])
    Y = len(data)
    n_of_XMAS = 0
    coordinates = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                coordinates.append((i,j))
    for coordinate in coordinates:
        i = coordinate[0]
        j = coordinate[1]
        if i + 3 < X and data[i + 1][j] == 'M' and data[i+2][j] == 'A' and data[i + 3][j] == 'S':
            n_of_XMAS += 1
        if i + 3 < X and j + 3 < Y and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
            n_of_XMAS += 1
        if j + 3 < Y and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
            n_of_XMAS += 1
        if i + 3 < X and j - 3 >= 0 and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
            n_of_XMAS += 1
        if j - 3 >= 0 and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
            n_of_XMAS += 1
        if i - 3 >= 0 and j - 3 >= 0 and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
            n_of_XMAS += 1
        if i - 3 >= 0 and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
            n_of_XMAS += 1
        if i - 3 >= 0 and j + 3 < Y and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
            n_of_XMAS += 1
    return n_of_XMAS


def find_X_MAS(data):
    X, Y = len(data[0]), len(data)
    n_of_X_MAS = 0
    coordinates = []
    for i in range(Y):
        for j in range(X):
            if data[i][j] == 'A':
                coordinates.append((i,j))
    for coordinate in coordinates:
        i, j = coordinate
        if 0 <= i-1 and i+1 < Y and 0 <= j-1 and j+1 < X:
            if data[i-1][j-1] == 'M' and data [i+1][j+1] == 'S':
                if data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S':
                    n_of_X_MAS += 1
                elif data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M':
                    n_of_X_MAS += 1
                else: pass
            elif data[i-1][j-1] == 'S' and data [i+1][j+1] == 'M':
                if data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S':
                    n_of_X_MAS += 1
                elif data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M':
                    n_of_X_MAS += 1
                else: pass
    return n_of_X_MAS


def main():
    with open("2024/Day 4/input.txt") as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    data = [list(x) for x in data]
        
    print("****Part 1****")
    print(find_XMAS(data))
    print("****Part 2****")
    print(find_X_MAS(data))

if __name__ == "__main__":
    main()
