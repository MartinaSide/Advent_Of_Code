import functools

with open("day12.txt") as file:
    input_lines = [line.split() for line in file.readlines()]


def parse_counts(counts):
    return tuple(int(i) for i in counts.split(","))


def repeat5(val: str, joiner: str) -> str:
    return joiner.join(val for _ in range(5))


@functools.cache
def count_matches(pattern, expected_dmg_count, pattern_index, cur_damaged_count, cur_count_idx, override_char=None):
    if pattern_index >= len(pattern):
        if cur_count_idx == len(expected_dmg_count) or (
                cur_count_idx + 1 == len(expected_dmg_count) and cur_damaged_count == expected_dmg_count[
            cur_count_idx]):
            return 1
        else:
            return 0

    if override_char == "#" or pattern[pattern_index] == "#":
        if cur_count_idx >= len(expected_dmg_count) or expected_dmg_count[cur_count_idx] < cur_damaged_count + 1:
            return 0

        return count_matches(pattern, expected_dmg_count, pattern_index + 1, cur_damaged_count + 1, cur_count_idx)
    elif override_char == "." or pattern[pattern_index] == ".":
        if cur_damaged_count > 0:
            if expected_dmg_count[cur_count_idx] != cur_damaged_count:
                return 0
            cur_count_idx += 1
            cur_damaged_count = 0

        return count_matches(pattern, expected_dmg_count, pattern_index + 1, cur_damaged_count, cur_count_idx)
    else:
        return count_matches(pattern, expected_dmg_count, pattern_index, cur_damaged_count, cur_count_idx, "#") + \
            count_matches(pattern, expected_dmg_count, pattern_index, cur_damaged_count, cur_count_idx, ".")


puzzle_input = [(pattern, parse_counts(counts_string)) for pattern, counts_string in input_lines]
print("Part 1:", sum(count_matches(pattern, counts, 0, 0, 0) for pattern, counts in puzzle_input))

puzzle_input = [(repeat5(pattern, "?"), parse_counts(repeat5(counts_string, ","))) for pattern, counts_string in
                input_lines]
print("Part 2:", sum(count_matches(pattern, counts, 0, 0, 0) for pattern, counts in puzzle_input))