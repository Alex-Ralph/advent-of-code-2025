from functools import cache
import re

def parse_data():
    with open("input/day02.txt") as file:
        return list((x.split("-") for x in file.read().split(",")))

# Disclaimer: I only realised this could be regexed after it was pointed out to me
# This is not the first solution I used
def sum_invalid_range_p1(start: str, end: str) -> int:
    return sum(x for x in range(int(start), int(end)+1) if re.fullmatch(r"([0-9]+)\1", str(x)))

def sum_invalid_range_p2(start: str, end: str) -> int:
    return sum(x for x in range(int(start), int(end)+1) if re.fullmatch(r"([0-9]+)\1+", str(x)))

print(f"Part one: {sum(sum_invalid_range_p1(x[0], x[1]) for x in parse_data())}")
print(f"Part two: {sum(sum_invalid_range_p2(x[0], x[1]) for x in parse_data())}")

