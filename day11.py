from functools import cache

from session import AdventOfCodeSession

adj = {}
for line in AdventOfCodeSession(day=11).puzzle_input.splitlines():
    start, neighbors = line.split(": ")
    adj[start] = neighbors.split()


@cache
def search(curr, dac=True, fft=True):
    if curr == "out":
        if dac and fft:
            return 1
        return 0
    total = 0
    for vector in adj[curr]:
        total += search(vector, dac or vector == "dac", fft or vector == "fft")
    return total


p1 = search("you", True, True)
p2 = search("svr", False, False)

print(p1, p2)
