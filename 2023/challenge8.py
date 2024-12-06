def sum_of_line(line):
    # replace all double spaces with single spaces
    line = line.replace("  ", " ")
    # split the line on ":" and "|"
    parts = line.split(":")
    card_number = parts[0].strip()
    numbers = parts[1].split("|")
    # find the intersection of the sets
    common_amount = how_many_same_numbers(numbers[0].split(), numbers[1].split())
    # return the size of the intersection
    if common_amount == 0:
        return 0, 0
    result = 2 ** (common_amount-1), common_amount
    return result


def from_line_get_numbers(line):
    # replace all double spaces with single spaces
    line = line.replace("  ", " ")
    # split the line on ":" and "|"
    parts = line.split(":")
    card_number = parts[0].strip()
    numbers = parts[1].split("|")
    # find the intersection of the sets
    common_amount = how_many_same_numbers(numbers[0].split(), numbers[1].split())
    return common_amount


def how_many_same_numbers(left, right):
    left_set = set(map(int, left))
    right_set = set(map(int, right))
    common_set = left_set & right_set
    len_common_set = len(common_set)
    return len_common_set


def read_file_and_process(filename):
    result = 0
    # Open the file in read mode
    with open(filename, "r") as f:
        number_of_lines = 215
        sums = number_of_lines*[1]
        for i, line in enumerate(f):
            line = line.strip()
            duplicates = from_line_get_numbers(line)
            print(f"Alla riga {i}: {duplicates} e carte: {sums[i]}")
            for j in range(1, duplicates+1):
                if i+j <= 215:
                    sums[i+j] += 1*sums[i]
                    print(i+j)
            result += sums[i]
    return result

print(read_file_and_process("challenge7_text.txt"))
