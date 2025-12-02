from functools import cache

def parse_data():
    with open("input/day02.txt") as file:
        return list((x.split("-") for x in file.read().split(",")))

def sum_invalid_range_p1(start: str, end: str) -> int:
    invalid = []
    for x in range(int(start), int(end)+1):
        num = str(x)
        if len(num) % 2 != 0:
            continue
        mid = int(len(num) / 2)
        if num[:mid] == num[mid:]:
            invalid.append(x)
    return sum(invalid)

@cache
def check_valid_id(id: str) -> bool:
    for pattern_len in range(1, int(len(id)/2)+1):
        if len(id) % pattern_len != 0:
            continue
        pattern = id[0:pattern_len]
        if id == pattern * int(len(id) / pattern_len):
            return False
    return True

def sum_invalid_range_p2(start: str, end: str) -> int:
    out = sum(x for x in range(int(start), int(end)+1) if not check_valid_id(str(x)))
    return out

print(f"Part one: {sum(sum_invalid_range_p1(x[0], x[1]) for x in parse_data())}")
print(f"Part two: {sum(sum_invalid_range_p2(x[0], x[1]) for x in parse_data())}")

