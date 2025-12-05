from session import AdventOfCodeSession

session = AdventOfCodeSession(day=5)

range_list, id_list = session.puzzle_input.split("\n\n")
ranges = [list(map(int, range.split("-"))) for range in range_list.split()]
ranges.sort(key=lambda range: range[0])

coalesced = [ranges[0]]
for start, end in ranges:  # [3-5, 10-14, 16-20, 12-18] -> [3-5, 10-20]
    if start <= coalesced[-1][1]:
        coalesced[-1][1] = max(coalesced[-1][1], end)
    else:
        coalesced.append([start, end])

ids = map(int, id_list.split())
p1 = sum(any(l <= n <= r for l, r in coalesced) for n in ids)
p2 = sum(end - start + 1 for start, end in coalesced)

print(p1, p2)
