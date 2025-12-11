from session import AdventOfCodeSession

adj = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
data = AdventOfCodeSession(day=4).puzzle_input.splitlines()

p1 = p2 = 0
initial_rolls = set()
for y, row in enumerate(data):
    for x, col in enumerate(row):
        if col == "@":
            initial_rolls.add((y, x))

removed_rolls = set()
while True:
    flag = False
    current_rolls = initial_rolls - removed_rolls

    for y, x in current_rolls:
        neighbors = map(lambda d: (y + d[0], x + d[1]) in current_rolls, adj)
        if sum(neighbors) < 4:
            removed_rolls.add((y, x))
            flag = True

    p1 = p1 or len(removed_rolls)
    if not flag:
        break

p2 = len(removed_rolls)
print(p1, p2)
