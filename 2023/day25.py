from itertools import combinations, pairwise
from functools import lru_cache
import random
from collections import Counter

import networkx as nx

with open("day25.txt") as fh:
    data = fh.read()

testdata = """\
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

def parse_puzzle(puzzle):
    L = []
    for line in puzzle.splitlines():
        node, others = line.split(": ")
        L.append((node, others.split()))
    return L


def load_graph(puzzle):
    G = nx.Graph()
    for node, others in parse_puzzle(puzzle):
        for other in others:
            G.add_edge(node, other)
    return G

G = load_graph(data)

try:
    del d1
except NameError:
    pass


@lru_cache(maxsize=None)
def d1(node):
    return nx.descendants_at_distance(G, node, 1)

nodes = list(G)
len(nodes)

cut_candidates = {
    frozenset((a, b)) for (a, b) in combinations(G, 2) if b in d1(a) and not (d1(a) & d1(b))
}
len(cut_candidates)

random.choices(nodes, k=2)

nx.shortest_path(G, *random.choices(nodes, k=2))

c = Counter()
for _ in range(1000):
    for edge in pairwise(nx.shortest_path(G, *random.choices(nodes, k=2))):
        edgefs = frozenset(edge)
        if edgefs in cut_candidates:
            c[edgefs] += 1

c.most_common(10)

[tuple(edgefs) for (edgefs, count) in c.most_common(3)]

G1 = G.copy()
G1.remove_edges_from(tuple(edgefs) for (edgefs, count) in c.most_common(3))
cc = list(nx.connected_components(G1))
if len(cc) == 2:
    print(len(cc[0]) * len(cc[1]))