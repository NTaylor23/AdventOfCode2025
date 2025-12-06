from functools import reduce
from itertools import islice
from operator import add, mul
from re import findall

from session import AdventOfCodeSession

data = AdventOfCodeSession(day=6).puzzle_input.splitlines()


def flip(numbers):
    sp = [list(item) for item in numbers]
    return filter(lambda n: n.isdigit(), ["".join(col).strip() for col in zip(*sp)])


operators = findall(r"[\+\*]+\s+", data.pop())
rows = []
for line in data:
    it = iter(line)
    rows.append(["".join(islice(it, None, length)) for length in map(len, operators)])


p1 = p2 = 0
for j in range(len(rows[0]) - 1, -1, -1):
    numbers = [rows[i][j] for i in range(len(rows))]
    operator = mul if operators.pop().strip() == "*" else add
    initial = int(operator is mul)  # initial value 1 if multiplying, 0 if adding
    
    p1 += reduce(operator, map(int, numbers), initial)
    p2 += reduce(operator, map(int, flip(numbers)), initial)

print(p1, p2)
