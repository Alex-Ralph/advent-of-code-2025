from functools import reduce

def parse_data():
    with open("test/day03.txt") as file:
        battery_strings = file.read().splitlines()
        return [[int(x) for x in battery] for battery in battery_strings]
    
def max_joltage(battery: list[int], digits: int):
    if digits == 0:
        return 0
    index, cell = reduce(lambda x, y: x if x[1] >= y[1] else y, enumerate(battery[:len(battery)-digits+1]))
    return cell * (10 ** (digits-1)) + max_joltage(battery[index+1:], digits-1)

batteries = parse_data()
print(sum([max_joltage(x, 2) for x in batteries]))
print(sum([max_joltage(x, 12) for x in batteries]))