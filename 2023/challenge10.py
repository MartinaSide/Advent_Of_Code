def read_data(filename):
    data = {}
    seeds = []
    category = None
    with open(filename) as f:
        first_line = f.readline().split(":")
        seeds = first_line[1].strip().split()
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                category = line[:-1]
                data[category] = []
            else:
                data[category].append(list(map(int, line.split())))
    seeds = list(zip(seeds[::2], seeds[1::2]))
    return seeds, data


def sort_map(map_to_sort):
    sorted_map = map_to_sort
    index = 0
    for i in range(0, len(sorted_map)):
        if sorted_map[index][1] > sorted_map[i][1]:
            sorted_map[index], sorted_map[i] = sorted_map[i], sorted_map[index]
            index = i
    return sorted_map


def transform(seeds, data):
    current_data = seeds.copy()
    next_data = []
    # Define the order of the categories as a list of strings
    categories = ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map",
                  "water-to-light map", "light-to-temperature map",
                  "temperature-to-humidity map", "humidity-to-location map"]
    # Loop through the categories list
    for category in categories:
        # Get the map from the data dictionary by using the pop method and passing the category name
        map = data.pop(category)
        sorted_map = sort_map(map)
        for start, length in current_data:
            temp_data = my_convert(start, length, sorted_map)
            for i in range (0, len(temp_data)):
                next_data.append(temp_data[i])
        current_data = next_data
        next_data = []
    return current_data


def my_convert(source_start, source_range_end, map):
    source_start = int(source_start)
    source_range_end = int(source_range_end)
    transformed = []
    while source_range_end > 0:
        for dest_range_start, source_map_range_start, map_length in map:
            difference_beginning = source_start - source_map_range_start
            difference_end = source_range_end + source_start - source_map_range_start
            if difference_end >= 0 > difference_beginning:
                transformed.append([source_start, -difference_beginning])
                source_start = source_start - difference_beginning
                source_range_end += difference_beginning
                difference_beginning = source_start - source_map_range_start
                difference_end = source_range_end + source_start - source_map_range_start
            if 0 < difference_beginning <= map_length:
                used_range = map_length - difference_beginning
                source_range_end -= used_range
                new_dest_start = dest_range_start + difference_beginning
                source_start += used_range
                transformed.append([new_dest_start, used_range])
            elif 0 <= difference_end <= map_length:
                used_range = difference_end
                new_dest_start = dest_range_start
                source_range_end -= used_range
                transformed.append([new_dest_start, used_range])
        if source_range_end > 0:
            transformed.append([source_start,source_range_end])
        source_range_end = 0
    return transformed


def find_min(array):
    min = array[0][0]
    for i in range(0, len(array)):
        if int(array[i][0]) < min:
            min = array[i][0]
    return min


one, two = read_data("challenge9_text.txt")
final_array = transform(one,two)
print(final_array)
miny = find_min(final_array)
print(miny)
