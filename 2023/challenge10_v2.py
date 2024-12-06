import os


class Ranges:

    def __init__(self, ranges):
        self._ranges = sorted(ranges, key=lambda rng: rng[1])

    def get_destination(self, source_val):
        """
        Returns the destination value corresponding to the source value, based on the ranges stored in self._ranges.

        Parameters:
        source_val: a numeric value that represents the source value to be mapped to a destination value.

        Returns:
        dest_value: a numeric value that represents the destination value corresponding to the source value,
        based on the ranges stored in self._ranges. If the source value does not fall within any of the ranges,
        the destination value is the same as the source value.

        Preconditions:
        self._ranges is a non-empty list of tuples of the form (dest, src, length), where dest, src, and length
        are numeric values, and length is positive.
        source_val is a numeric value.

        Postconditions:
        dest_value is a numeric value. (dest_value = destination value)
        dest_value is equal to source_val, or dest_value is equal to dest + (source_val - src) for some (dest, src,
        length) in self._ranges, where source_val >= src and source_val < src + length.

        Invariants:
        self._ranges does not change during the execution of the method.
        """
        dest_value = source_val
        for dest, src, length in self._ranges:
            if source_val < src:
                return dest_value
            if src <= source_val < src + length:
                return dest + (source_val - src)
        return dest_value

    def get_destination_ranges(self, source_range):
        """
        Returns a list of destination ranges corresponding to the source range, based on the ranges stored in
         self._ranges.

        Parameters:
        source_range: a tuple of the form (start, end), where start and end are numeric values, representing a range
        of source values to be mapped to destination ranges.

        Returns:
        result: a list of tuples of the form (start, end), where start and end are numeric values, representing the
        destination ranges corresponding to the source range, based on the ranges stored in self._ranges. If the
        source range does not overlap with any of the ranges in self._ranges, the destination range is the same
        as the source range.

        Preconditions:
        self._ranges is a non-empty list of tuples of the form (dest, src, length), where dest, src, and length
        are numeric values, and length is positive.
        source_range is a tuple of the form (start, end), where start and end are numeric values, and start <= end.

        Postconditions:
        result is a non-empty list of tuples of the form (start, end), where start and end are numeric values,
        and start <= end.
        result is the union of the destination ranges that overlap with the source range, based on the ranges
        stored in self._ranges. If the source range does not overlap with any of the ranges in self._ranges,
        result is [source_range].

        Invariants:
        self._ranges does not change during the execution of the method.
        Ranges._calc_overlap is a static method that takes two tuples of the form (start, end) and returns a
        list of tuples of the form (range, overlaps), where range is a tuple of the form (start, end), and
        overlaps is a boolean value indicating whether the range overlaps with the second tuple or not.
        """
        result = []
        unmappeds = [source_range]
        for r in self._ranges:
            new_unmappeds = []
            for unmapped in unmappeds:
                parts = Ranges._calc_overlap(unmapped, (r[1], r[2]))
                for rng, overlaps in parts:
                    if overlaps:
                        result.append((rng[0] + r[0] - r[1], rng[1]))
                    else:
                        new_unmappeds.append(rng)
            unmappeds = new_unmappeds
        result += unmappeds
        return result

    def get_all_destination_ranges(self, source_ranges):
        result = []
        for source_range in source_ranges:
            result += self.get_destination_ranges(source_range)
        return set(result)

    @staticmethod
    def _calc_overlap(first_range, second_range):
        """
        Returns a list of tuples that represent the overlapping and non-overlapping parts of two ranges.

        Parameters:
        rng: a tuple of the form (min1, len1), where min1 and len1 are numeric values, representing the first range.
        other: a tuple of the form (min2, len2), where min2 and len2 are numeric values, representing the second range.

        Returns:
        result: a list of tuples of the form (range, overlaps), where range is a tuple of the form (start, end),
        and overlaps is a boolean value indicating whether the range overlaps with the second range or not.
        The list contains at most three tuples, corresponding to the left, middle, and right parts of the
        first range, relative to the second range.

        Preconditions:
        rng and other are tuples of the form (min, len), where min and len are numeric values, and len is positive.

        Postconditions:
        result is a list of tuples of the form (range, overlaps), where range is a tuple of the form (start, end),
        and overlaps is a boolean value.
        result is the result of splitting the first range into subranges that either overlap or do not overlap
        with the second range. The subranges are contiguous and cover the entire first range. The order of the
        subranges in the list is the same as the order of the subranges in the first range.
        If the first range does not overlap with the second range at all, result is [(rng, False)].

        Invariants:
        rng and other do not change during the execution of the method.
        """
        min1, len1 = first_range
        min2, len2 = second_range
        overlap_min = max(min1, min2)
        overlap_max = min(min1 + len1, min2 + len2)
        if overlap_min < overlap_max:
            result = []
            if min1 < overlap_min:
                result.append(((min1, overlap_min - min1), False))
            overlap = (overlap_min, overlap_max - overlap_min)
            result.append((overlap, True))
            if min1 + len1 > overlap_max:
                result.append(((overlap_max, min1 + len1 - overlap_max), False))
            return result
        else:
            return [(first_range, False)]


def read_input(filename):
    with open(filename) as f:
        result = f.readlines()
    return result


def parse_seeds(lines, line_num):
    line = lines[line_num]
    seeds = line.split(":")[1].split()
    return [int(seed) for seed in seeds], line_num + 1


def skip_empty_lines(lines, line_num):
    lines_len = len(lines)
    while line_num < lines_len:
        line = lines[line_num]
        if not line.strip():
            line_num += 1
        else:
            break
    return line_num


def parse_ranges(lines, line_num):
    lines_len = len(lines)
    line_num += 1
    ranges = []
    while line_num < lines_len:
        line = lines[line_num]
        if not line.strip():
            break
        line_num += 1
        ranges.append([int(i) for i in line.split()])
    return Ranges(ranges), line_num


def get_final_dest_value(source_value, ranges_list):
    ret = source_value
    for ranges in ranges_list:
        ret = ranges.get_destination(ret)
    return ret


def get_final_dest_ranges(source_ranges, ranges_list):
    result = source_ranges
    for ranges in ranges_list:
        result = ranges.get_all_destination_ranges(result)
    return result


lines = read_input(os.path.dirname(__file__) + os.sep + "challenge9_text.txt")
line_num = 0

ranges, line_num = parse_seeds(lines, line_num)
seed_ranges = []
n = len(ranges) // 2
for i in range(n):
    start = ranges[2 * i]
    length = ranges[2 * i + 1]
    seed_ranges.append((start, length))

line_num = skip_empty_lines(lines, line_num)
seed_soil, line_num = parse_ranges(lines, line_num)

line_num = skip_empty_lines(lines, line_num)
soil_fert, line_num = parse_ranges(lines, line_num)

line_num = skip_empty_lines(lines, line_num)
fert_water, line_num = parse_ranges(lines, line_num)

line_num = skip_empty_lines(lines, line_num)
water_light, line_num = parse_ranges(lines, line_num)

line_num = skip_empty_lines(lines, line_num)
light_temp, line_num = parse_ranges(lines, line_num)

line_num = skip_empty_lines(lines, line_num)
temp_humid, line_num = parse_ranges(lines, line_num)

line_num = skip_empty_lines(lines, line_num)
humid_location, line_num = parse_ranges(lines, line_num)

ranges_list = [
    seed_soil,
    soil_fert,
    fert_water,
    water_light,
    light_temp,
    temp_humid,
    humid_location
]

location_ranges = get_final_dest_ranges(seed_ranges, ranges_list)

lowest_location = None
for loc_range in location_ranges:
    location = loc_range[0]
    if lowest_location is None or location < lowest_location:
        lowest_location = location

print(lowest_location)
