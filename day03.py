from session import AdventOfCodeSession

session = AdventOfCodeSession(day=3)


def get_output(bank, sz):
    stack = []
    for i, val in enumerate(bank):
        while stack and stack[-1] < val and (len(stack) + len(bank) - i) > sz:
            stack.pop()
        if len(stack) < sz:
            stack.append(val)
    return int("".join(str(n) for n in stack))


p1 = p2 = 0
for line in session.puzzle_input.splitlines():
    digits = list(map(int, list(line)))
    p1 += get_output(digits, 2)
    p2 += get_output(digits, 12)

print(p1, p2)
