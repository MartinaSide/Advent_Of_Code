import numpy as np
from itertools import combinations

with open("day11.txt", "r") as file:
    data = file.readlines()

m = np.zeros((len(data), len(data[0]) - 1))
for i, line in enumerate(data):
    m[i] = [char == "#" for char in line.strip()]

h = m.sum(axis=0) == 0
v = m.sum(axis=1) == 0

nodes = []
rp = 0
for r in range(m.shape[0]):
    if v[r]:
        rp += 1
    cp = 0
    for c in range(m.shape[1]):
        if h[c]:
            cp += 1
        if m[r, c]:
            nodes.append((rp, cp))
        cp += 1
    rp += 1

nodes = np.array(nodes)

print(int(sum([np.linalg.norm(p[0] - p[1], 1) for p in combinations(nodes, 2)])))
print(int(sum([np.linalg.norm(p[0] - p[1], 1) for p in combinations(nodes, 2)])))


from itertools import combinations as comb
L = [x.strip() for x in open('day11.txt')]
n,m,L_ = list(range(len(L))), list(range(len(L[0]))), list(zip(*L))
er,ec = {i for i in n if set(L[i]) == {'.'}},{j for j in m if set(L_[j]) == {'.'}}
galaxies = [ (i, j) for i in n for j in m if L[i][j] == '#' ]


def expand(i, j, by=1):
  return i + by*len(set(range(i))&er), j + by*len(set(range(j))&ec)


parts = [[expand(*g, i) for g in galaxies] for i in [1, 999_999]]
for part in parts:
  print(sum(abs(p[0][0]-p[1][0]) + abs(p[0][1]-p[1][1]) for p in list(comb(part, 2))))