from copy import copy

with open("input/day04.txt") as file:
    data = file.read()
    roll_coordinates = {
        x + y*1j 
        for y, line in enumerate(data.split("\n")) 
        for x, val in enumerate(line)
        if val == "@"
    }

neighbour_coords = {-1, +1, -1-1j, -1j, 1-1j, -1+1j, 1j, 1+1j}
accessible = {coord for coord in roll_coordinates if
        len(roll_coordinates & {coord + x for x in neighbour_coords}) < 4
    }

print(f"Part one: {len(accessible)}")

rolls_after_move = roll_coordinates - accessible
while len(accessible) != 0:
    accessible = {coord for coord in rolls_after_move if
        len(rolls_after_move & {coord + x for x in neighbour_coords}) < 4
    }
    rolls_after_move -= accessible


print(f"Part two: {len(roll_coordinates) - len(rolls_after_move)}")