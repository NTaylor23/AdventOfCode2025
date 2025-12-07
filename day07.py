from functools import cache

from session import AdventOfCodeSession

data = AdventOfCodeSession(day=7).puzzle_input.splitlines()

start, p1, splitters = data[0].index("S"), 0, {}
for y, line in enumerate(data):
    splitters[y] = {x for x, col in enumerate(line) if col == "^"}


beams = set([start])
for y in range(len(data)):
    hits = beams & splitters[y]
    for hit in hits:
        beams |= {hit - 1, hit + 1}
        beams.remove(hit)
    p1 += len(hits)


@cache
def get_timelines(row, pos):
    for y in range(row, len(data)):
        if pos in splitters[y]:
            return get_timelines(y, pos - 1) + get_timelines(y, pos + 1)
    return 1


p2 = get_timelines(0, start)
print(p1, p2)
