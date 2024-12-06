def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    bucket = [0] * (max_val - min_val + 1)
    for i in range(len(arr)):
        bucket[arr[i] - min_val] += 1
    arr.clear()
    for i in range(len(bucket)):
        arr += [i + min_val] * bucket[i]
    return arr


def main():
    first_arr = []
    second_arr = []
    with open("2024/Day 1/input.txt") as f:
        data = f.read().splitlines()
        for line in data:
            number = line.split("   ")
            first_arr.append(int(number[0]))
            second_arr.append(int(number[1]))
    assert len(first_arr) == len(second_arr)
    first_arr = bucket_sort(first_arr)
    second_arr = bucket_sort(second_arr)
    for i in range(len(first_arr)):
        difference_arr = [abs(first_arr[i] - second_arr[i]) for i in range(len(first_arr))]
    print("****Part 1****")
    print(sum(difference_arr))

    hash_table_first_arr = {}
    hash_table_second_arr = {}
    for i in range(len(first_arr)):
        hash_table_first_arr[first_arr[i]] = hash_table_first_arr.get(first_arr[i], 0) + 1
        hash_table_second_arr[second_arr[i]] = hash_table_second_arr.get(second_arr[i], 0) + 1
    print("****Part 2****")
    similarity_score = 0
    for key in hash_table_first_arr:
        if key in hash_table_second_arr:
            similarity_score += key * hash_table_first_arr[key] * hash_table_second_arr[key]
    print(similarity_score)


if __name__ == "__main__":
    main()
