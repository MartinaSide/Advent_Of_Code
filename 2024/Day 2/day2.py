def is_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def is_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            return False
    return True


def is_sorted(numbers):
    if len(numbers) == 0:
        return False
    if numbers[0] < numbers[1]:
        if is_increasing(numbers):
            return True
    elif numbers[0] > numbers[1]:
        if is_decreasing(numbers):
            return True
    else:
        if is_decreasing(numbers) or is_increasing(numbers):
            return True
    return False

def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))


def is_diff_legal(numbers, max_diff = 3):
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) > max_diff:
            return False
    return True

def is_safe(numbers):
    return is_sorted(numbers) and not has_duplicates(numbers) and is_diff_legal(numbers)


def main():
    with open("2024/Day 2/input.txt") as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    illegal_reports = []

    safe = 0
    for line in data:
        numbers = line.split(" ")
        numbers = [int(x) for x in numbers]
        if not is_sorted(numbers):
            illegal_reports.append(numbers)
            continue
        if has_duplicates(numbers):
            illegal_reports.append(numbers)
            continue
        if is_diff_legal(numbers):
            safe += 1   
        else:
            illegal_reports.append(numbers)
    print("****Part 1****")
    print(safe)
    print("****Part 2****")
    for report in illegal_reports:
        for i in range(len(report)):
            temp = report[:i] + report[i + 1:]
            if is_safe(temp):
                safe += 1
                break
    print(safe)



if __name__ == "__main__":
    main()
