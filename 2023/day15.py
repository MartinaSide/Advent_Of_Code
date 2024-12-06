from collections import defaultdict

from aoc import input_as_string, print_matrix

inp = input_as_string("day15.txt").split(",")


def hash(a):
    ss = 0
    for char in a:
        ss += ord(char)
        ss *= 17
        ss %= 256
    return ss


s1 = 0
for a in inp:
    s1 += hash(a)

print(s1)

# PART 2
boxes = defaultdict(list)

for a in inp:
    if "=" in a:
        label = a[:-2]
        bucket = hash(label)
        fl = int(a[-1])
        found_lens = False
        for lens in boxes[bucket]:
            if lens[0] == label:
                lens[1] = fl
                found_lens = True
        if not found_lens:
            boxes[bucket].append([label, fl])
    else:
        label = a[:-1]
        bucket = hash(label)
        idx = [i for i, x in enumerate(boxes[bucket]) if x[0] == label]
        if len(idx) > 0:
            del boxes[bucket][idx[0]]

s2 = 0
for box in boxes.keys():
    a1 = box + 1
    for idx, lens in enumerate(boxes[box]):
        a2 = idx + 1
        a3 = lens[1]
        s2 += a1 * a2 * a3

print(s2)
