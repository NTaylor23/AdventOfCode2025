from itertools import combinations
from math import dist

from session import AdventOfCodeSession

data = AdventOfCodeSession(day=8).puzzle_input.splitlines()

p1 = p2 = 0
boxes = [tuple(int(sp) for sp in line.split(",")) for line in data]
dist_pairs = [(*pair, dist(*pair)) for pair in combinations(boxes, 2)]

circuits = []

for i, (p, q, _) in enumerate(sorted(dist_pairs, key=lambda pair: pair[2])):
    s = {p, q}
    for circuit in circuits:
        if p not in circuit and q not in circuit:
            continue
        tmp = [c for c in circuits if p not in c and q not in c]
        for box in filter(lambda c: p in c or q in c, circuits):
            s |= box
        tmp.append(s)
        circuits = tmp
        break
    else:
        circuits.append(set([p, q]))

    if i == 1000:
        lengths = sorted([len(c) for c in circuits], reverse=True)[:3]
        p1 = lengths[0] * lengths[1] * lengths[2]
    if len(circuits) == 1 and len(circuits[0]) == len(data):
        p2 = p[0] * q[0]
        break

print(p1, p2)
