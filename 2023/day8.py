from math import lcm
from itertools import cycle
from re import findall

commands, _, *lines = open("day8.txt", "r").readlines()
paths_dict = dict((key, (node1, node2)) for (key, node1, node2) in map(lambda line: findall(r"[A-Z]+", line), lines))


def part1():
    key = "AAA"
    for i, command in enumerate(cycle(commands.strip()), 1):
        key = paths_dict[key][command == "R"]
        if key == "ZZZ":
            return i


def part2():
    results = []
    for key in [i for i in paths_dict.keys() if i.endswith("A")]:
        for i, command in enumerate(cycle(commands.strip()), 1):
            key = paths_dict[key][command == "R"]
            if key.endswith("Z"):
                results.append(i)
                break
    return lcm(*results)


print(f"The solution for the first part is: {part1()}")
print(f"The solution for the second part is: {part2()}")
