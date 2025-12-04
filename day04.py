


def parse_data():
    with open("input/day04.txt") as file:
        data = file.read()
        max_x = len(data.split("\n")[0]) + 1
        max_y = len(data.split("\n")) + 1
        map = {x+1 + y*1j+1j: val for y, line in enumerate(data.split("\n"))
                for x, val in enumerate(line)}
        map.update({x+0j: "." for x in range(max_x+1)})
        map.update({0 + y*1j: "." for y in range(max_y+1)})
        map.update({x + max_y*1j: "." for x in range(max_x+1)})
        map.update({max_x + y*1j: "." for y in range(max_y+1)})
    return max_x, max_y, map

max_x, max_y, map = parse_data()

def can_access(coord: complex, map: dict[complex: str]) -> bool:
    surroundings = (coord-1-1j, coord-1j, coord+1-1j,
                    coord-1, coord+1,
                    coord-1+1j, coord+1j, coord+1+1j)
    occupied_surroundings = sum(map[x] == "@" for x in surroundings)
    return occupied_surroundings < 4

print(sum(can_access(x+y*1j, map) for y in range(1, max_y) for x in range(1, max_x) if map[x+y*1j] == "@"))

def recursive_remove(coord_map: dict[complex: str]) -> dict[complex: str]:
    to_remove = [x for x, y in coord_map.items() if y == "@" and can_access(x, coord_map)]
    if len(to_remove) == 0:
        return coord_map
    new_map = {coord: ("." if coord in to_remove else char) for coord, char in coord_map.items()}
    return recursive_remove(new_map)
 
final_map = recursive_remove(map)
print(list(map.values()).count("@") - list(final_map.values()).count("@"))
