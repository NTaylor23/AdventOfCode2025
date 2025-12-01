from session import AdventOfCodeSession

session = AdventOfCodeSession(day=1)

p1 = p2 = 0
pos = 50

for line in session.puzzle_input.splitlines():
    distance = int(line[1:])
    sign = 1 if line[0] == "R" else -1  # R = 1, L = -1

    delta = pos + distance * sign
    mn, mx = sorted((pos, delta))
    times_clicking_zero = abs(mn // 100) + abs(mx // 100)
    if sign < 0:
        times_clicking_zero -= int(pos == 0)
        times_clicking_zero += int(delta % 100 == 0)
    pos = delta % 100
    p1 += int(pos == 0)
    p2 += times_clicking_zero

print(p1, p2)
