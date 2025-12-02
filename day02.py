from math import ceil

from session import AdventOfCodeSession

session = AdventOfCodeSession(day=2)


def is_repeated_twice(n):
    s = str(n)
    return s[: len(s) // 2] == s[len(s) // 2 :]


p1 = p2 = 0

for start, end in [r.split("-") for r in session.puzzle_input.split(",")]:
    invalid_numbers = set()

    for length in range(len(start), len(end) + 1):
        for i in range(1, (len(end) // 2) + 1):
            # either the first digits up to `i` of `start``,
            # or 1 if `end` has more digits than `start`
            # and we have to try digits beyond 9
            initial_value = int(start[:i]) if length == len(start) else 1

            for val in range(initial_value, 10**i):
                # try creating strings of the same length as `start` or `end`
                # that are made of repeated substrings from digits in either
                number = int(str(val) * ceil(length / i))
                if number < int(start) or number <= 10 or number in invalid_numbers:
                    continue
                if number > int(end):
                    break
                invalid_numbers.add(number)

    p1 += sum(filter(lambda n: is_repeated_twice(n), invalid_numbers))
    p2 += sum(invalid_numbers)

print(p1, p2)
