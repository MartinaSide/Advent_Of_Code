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
            if check_game_possible(line):
                result += i + 1
            # Print the result
            print(f"Result for line {i+1}: {result}")
    return result


def is_combination_possible(a):
    if a[0] <= 12 and a[1] <= 13 and a[2] <= 14:
        return True
    return False


# This method splits the string on ";", it initalizes an array a=[0,0,0] and for every element of the array that's been given
# if the last character in the element of the array is "d", it reads the first two characters of the element of the array and transforms any " " and then transforms it into a numeral and adds it to the first position of a,
# if the last character in the element of the array is "n", it reads the first two characters of the element of the array and transforms any " " and then transforms it into a numeral and adds it to the second position of a,
# if the last character in the element of the array is "e", it reads the first two characters of the element of the array and transforms any " " and then transforms it into a numeral and adds it to the third position of a.
# On the last element of the array, it checks if  if the first position is <=12, the second <=13 and the third <=14 and returns False if it's wrong. Otherwise, at the end it returns true
def check_game_possible(input_string):
    temp_parts = input_string.split(":")
    parts = temp_parts[1].split(";")
    a = [0, 0, 0]
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
        if not is_combination_possible(a):
            print(a)
            return False
    return True


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