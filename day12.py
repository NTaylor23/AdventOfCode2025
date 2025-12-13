from collections import defaultdict
from re import findall

from session import AdventOfCodeSession

data = AdventOfCodeSession(day=12).puzzle_input.split("\n\n")
shapes = defaultdict(list)

for section in data[:-1]:
    idx, shape = section.split(":")
    shapes[int(idx)] = shape.count("#")

p1 = 0
for line in data.pop().strip().split("\n"):
    rows, cols, *amts = map(int, findall(r"\d+", line))
    if sum(shapes[i] * amt for i, amt in enumerate(amts)) > rows * cols:
        continue
    p1 += 1

print(p1)
