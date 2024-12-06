# This method reads an input file row by row and calls another method that has that row as an argument
def read_file_and_process(filename):
    result = 0
    # Open the file in read mode
    with open(filename, "r") as f:
        # Loop through each line in the file
        for i, line in enumerate(f):
            # Strip the newline character from the line
            line = line.strip()
            # Call the get_sum_of_games method with the line as an argument
            result += power_of_set_of_cubes(check_game_min(line))
            # Print the result
            print(f"Result for line {i+1}: {result}")
    return result


def power_of_set_of_cubes(a):
    result = a[0]*a[1]*a[2]
    return result


def min_balls(first_array, second_array):
    c = first_array
    if first_array[0] < second_array[0]:
        c[0] = second_array[0]
    if first_array[1] < second_array[1]:
        c[1] = second_array[1]
    if first_array[2] < second_array[2]:
        c[2] = second_array[2]
    return c


def check_game_min(input_string):
    temp_parts = input_string.split(":")
    parts = temp_parts[1].split(";")
    b = [0, 0, 0]
    # Loop through the elements in the parts array
    for part in parts:
        a = [0, 0, 0]
        temp_game = part.split(",")
        for game in temp_game:
            # Check if the last character in the element is "d", "n", or "e"
            if game[-1] in ["d", "n", "e"]:
                numeral = remove_non_numeric(game)
                # Add the numeral to the corresponding position in the array
                if game[-1] == "d":
                    a[0] += numeral
                elif game[-1] == "n":
                    a[1] += numeral
                elif game[-1] == "e":
                    a[2] += numeral
        b = min_balls(b, a)
    return b


# This method takes a string as an argument and returns a new string that contains only numeric values
def remove_non_numeric(string):
    # Initialize an empty string to store the result
    result = ""
    # Loop through each character in the string
    for char in string:
        # Check if the character is a digit
        if char.isdigit():
            # Append the character to the result
            result += str(char)
    # Return the result
    return int(result)


print(read_file_and_process("challenge3_text.txt"))
