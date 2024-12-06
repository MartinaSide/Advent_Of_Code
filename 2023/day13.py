import numpy as np
from copy import deepcopy


def read_input(infile):
    with open(infile) as f:
        return [np.array(g) for g in [[list(l) for l in m.split("\n")] for m in f.read().strip("\n").split("\n\n")]]


def search_reflection(m, ignore=-1):
    # look for a potential horizontal line of reflection
    i = -1
    for i in range(len(m) - 1):
        if np.array_equal(m[i], m[i + 1]):
            # check if surfaces are mirrored
            top = m[:i + 1]
            bot = m[i + 1:]
            if len(top) < len(bot):
                bot = bot[:len(top)]
            elif len(bot) < len(top):
                top = top[len(top) - len(bot):]
            if np.array_equal(top, bot[::-1]):
                if ignore == -1:  # part 1
                    return i
                else:  # part 2 (needs to ignore original reflection)
                    if i != ignore:
                        return i
    return -1


def search_reflection_both_directions(m, ignore=(-1, -1)):
    # Part 2 needs to ignore original reflection when smudging elements in the non-reflected zone
    ji, ii = ignore
    # search for reflection over horizontal line
    j = search_reflection(m, ignore=ji - 1)  # beware! reflection is saved in number of rows, not index!
    if j != -1:
        return (j + 1, 0)
    else:
        # if not found, search for reflection over vertical line by rotating map
        mrot = np.rot90(m, k=3)
        i = search_reflection(mrot, ignore=ii - 1)  # beware! reflection is saved in number of columns, not index!
        if i != -1:
            return 0, i + 1
    return 0, 0


def part1(file_name):
    maps = read_input(file_name)
    refs = [search_reflection_both_directions(m) for m in maps]
    ctot, rtot = 0, 0
    for c, r in refs:
        ctot += c
        rtot += r
    return 100 * ctot + rtot


flip = {"#": ".", ".": "#"}


def search_reflection_smudge(m):
    row_old = search_reflection_both_directions(m)
    for j, l in enumerate(m):
        for i, v in enumerate(l):
            mnew = deepcopy(m)
            mnew[j, i] = flip[v]
            r = search_reflection_both_directions(mnew, ignore=row_old)
            if r != (0, 0) and r != row_old:
                return r
    return None


def part2(infile):
    maps = read_input(infile)
    refs = [search_reflection_smudge(m) for m in maps]
    ctot, rtot = 0, 0
    for c, r in refs:
        ctot += c
        rtot += r
    return 100 * ctot + rtot


print("Part 1:", part1("day13.txt"))
print("Part 2:", part2("day13.txt"))
