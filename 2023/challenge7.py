def sum_of_line(line):
  # replace all double spaces with single spaces
  line = line.replace("  ", " ")
  # split the line on ":" and "|"
  parts = line.split(":")
  card_number = parts[0].strip()
  numbers = parts[1].split("|")
  # find the intersection of the sets
  common_amount = how_many_same_numbers(numbers[0].split(),numbers[1].split())
  # return the size of the intersection
  if common_amount==-1:
      return 0
  result = 2**(common_amount)
  return result


def how_many_same_numbers(left, right):
    left_set = set(map(int,left))
    right_set = set(map(int,right))
    common_set = left_set & right_set
    len_common_set = len(common_set) - 1
    return len_common_set


def read_file_and_process(filename):
    result = 0
    # Open the file in read mode
    with open(filename, "r") as f:
        # Loop through each line in the file
        for i, line in enumerate(f):
            # Strip the newline character from the line
            line = line.strip()
            # Call the get_sum_of_games method with the line as an argument
            result += sum_of_line(line)
            # Print the result
            print(f"Result for line {i+1}: {result}")
    return result

print(read_file_and_process("challenge7_text.txt"))