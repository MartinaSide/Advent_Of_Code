def main():
    with open("2024/Day 4/input.txt") as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    
    data = [list(x) for x in data]
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
        elif i + 3 < X and j + 3 < Y and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
            n_of_XMAS += 1
        elif j + 3 < Y and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
            n_of_XMAS += 1
        elif i + 3 < X and j - 3 >= 0 and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
            n_of_XMAS += 1
        elif j - 3 >= 0 and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
            n_of_XMAS += 1
        elif i - 3 >= 0 and j - 3 >= 0 and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
            n_of_XMAS += 1
        elif i - 3 >= 0 and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
            n_of_XMAS += 1
        elif i - 3 >= 0 and j + 3 < Y and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
            n_of_XMAS += 1
        else:
            continue
        
    print("****Part 1****")
    print(n_of_XMAS)

if __name__ == "__main__":
    main()
