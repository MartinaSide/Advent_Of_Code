# Define a method that opens a file and reads the data
def read_data(filename):
    """
    Reads the data from a file and returns a dictionary of maps and a list of seeds.

    Input:
        filename: a string representing the name of the file to be read.

    Output:
        a tuple of (seeds, data), where:
            seeds: a list of strings representing the seed numbers.
            data: a dictionary of lists of lists of integers representing the maps between categories.

    Preconditions:
        - The file exists and is readable.
        - The file has a valid format, as described in the problem statement.
        - The file is not empty and has at least one line.

    Postconditions:
        - The seeds list contains the second part of the first line of the file, split on whitespace.
        - The data dictionary contains the rest of the lines of the file, grouped by categories that end with ":".
        - Each category in the data dictionary is a key that maps to a list of lists of integers, representing the destination range start, the source range start, and the range length for each line in that category.
        - The order of the categories and the lines within each category is preserved from the file.

    Invariants:
        - The filename is not modified by the method.
        - The seeds list and the data dictionary are not modified after they are returned by the method.
    """
    data = {}
    # Initialize an empty list to store the seeds
    seeds = []
    # Initialize a variable to store the current category
    category = None
    # Open the file in read mode
    with open(filename) as f:
        # Read the first line and split it on ":"
        first_line = f.readline().split(":")
        # Save the second part in "seeds" after stripping and splitting on whitespace
        seeds = first_line[1].strip().split()
        # Loop through the rest of the lines
        for line in f:
            # Strip the line
            line = line.strip()
            # If the line is empty, do nothing and continue to the next line
            if not line:
                continue
            # If the line ends with ":", create a new category and an empty list in the data dictionary
            if line.endswith(":"):
                category = line[:-1]
                data[category] = []
            # Otherwise, append the line as a list of integers to the data dictionary under the current category
            else:
                data[category].append(list(map(int, line.split())))
    # Return the data dictionary and the seeds list
    return seeds, data


# Define a function that converts a source number to a destination number using a map
def convert(source, map):
    """
    Converts a source number to a destination number using a map.

    Input:
        source: an integer representing the source number.
        map: a list of lists of integers representing the map between categories.

    Output:
        an integer representing the destination number.

    Preconditions:
        - The source number is a valid integer.
        - The map is a valid list of lists of integers, where each sublist has three elements: the destination range start, the source range start, and the range length.
        - The map is not empty and covers all the possible source numbers.

    Postconditions:
        - The output number is a valid integer.
        - The output number is in the range of the destination range start and the destination range start plus the range length for some sublist in the map, such that the source number is in the corresponding source range.
        - If the source number is not mapped, meaning that it is not in the range of the source range start and the source range start plus the range length for any sublist in the map, the output number is the same as the source number.

    Invariants:
        - The source number and the map are not modified by the function.
    """
    # Loop through each sublist in the map
    for dest_start, source_start, length in map:
        # Calculate the difference between the source number and the source range start
        diff = source - source_start
        # Check if the difference is greater than or equal to zero and less than the range length
        if 0 <= diff < length:
            # Return the difference added to the destination range start
            return dest_start + diff
    # If the loop ends without returning, the source number is not mapped
    # Return the same number as the destination number
    print(f"{source}: not found in range {map[0][1]}!!!")
    return source


# Define a method that applies all category transformations to the seed list
def transform_seeds(seeds, data):
    """
    Transforms the seed numbers to the final category numbers using the data dictionary of maps.

    Input:
        seeds: a list of strings representing the seed numbers.
        data: a dictionary of lists of lists of integers representing the maps between categories.

    Output:
        a list of integers representing the final category numbers for each seed.

    Preconditions:
        - The seeds list and the data dictionary are not empty and have valid values.
        - The data dictionary contains all the necessary categories and maps to transform the seeds.

    Postconditions:
        - The output list has the same length as the seeds list.
        - The output list contains the final category numbers for each seed after applying all the category transformations in the order given by the data dictionary.
        - Any source numbers that aren't mapped correspond to the same destination number.

    Invariants:
        - The seeds list and the data dictionary are not modified by the method.
    """
    # Initialize an empty list to store the output
    output = []
    # Loop through each seed in the seeds list
    for seed in seeds:
        # Convert the seed from a string to an integer
        seed = int(seed)
        # Initialize a variable to store the current number
        current = seed
        # Loop through each category and map in the data dictionary
        for category, map in data.items():
            # Convert the current number to the destination number using the map
            current = convert(current, map)
        # Append the current number to the output list
        output.append(current)
    # Return the output list
    return output


# Define a method that finds the smallest number in an array
def find_min(array):
    """
    Finds the smallest number in an array.

    Input:
        array: a list of numbers.

    Output:
        a number representing the smallest element in the array.

    Preconditions:
        - The array is not empty and contains only numbers.

    Postconditions:
        - The output number is the smallest element in the array.
        - The output number is unique, meaning that there is no other element in the array that is equal to it.

    Invariants:
        - The array is not modified by the method.
    """
    # Initialize a variable to store the smallest number
    min = array[0]
    # Loop through the rest of the elements in the array
    for num in array[1:]:
        # If the current element is smaller than the smallest number, update the smallest number
        if num < min:
            min = num
    # Return the smallest number
    return min


one, two = read_data("challenge9_text.txt")
final_array = transform_seeds(one,two)
print(find_min(final_array))
