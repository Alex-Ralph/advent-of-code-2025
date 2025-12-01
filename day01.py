from math import floor
def get_input():
    with open("input/day01.txt") as file:
        lines = file.read().splitlines()
        return [
            int(x[1:]) if x[0] == 'R' else -int(x[1:]) for x in lines
        ]

def part_one():
    turns = get_input()
    pos = 50
    password = 0
    for turn in turns:
        pos = (pos + turn) % 100
        if pos == 0:
            password += 1
    return password

def part_two():
    turns = get_input()
    pos = 50
    password = 0
    for turn in turns:
        password += abs(floor((pos + turn) / 100))
        if pos == 0 and turn < 0:
            password -= 1
        pos = (pos + turn) % 100
        if pos == 0 and turn < 0:
            password += 1
    return password



print(part_one())
print(part_two()) 