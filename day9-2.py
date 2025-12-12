
from itertools import chain
from functools import cache
with open("input/day09.txt") as file:
    red_tiles = [int(x[0]) + int(x[1])*1j for x in [y.split(",") for y in file.read().splitlines()]]
                #  for y, line in enumerate(file.read().splitlines()) 
                #  for x, val in enumerate(line)
                #  if val == "#"]
    
areas = []
for tile in red_tiles:
    tile_areas = [(tile, x, (abs((tile.real - x.real))+1) * (abs((tile.imag - x.imag))+1)) for x in red_tiles]
    areas += tile_areas
    
sorted_areas = sorted(areas, key=lambda x: x[2], reverse=True)
# part one
print(sorted_areas[0][2])

walls = set()
tile_pairs = zip(red_tiles, red_tiles[1:] + [red_tiles[0]])
for start_tile, end_tile in tile_pairs:
    if start_tile.real != end_tile.real:
        start_x = min(start_tile.real, end_tile.real)
        end_x = max(start_tile.real, end_tile.real)
        y = start_tile.imag
        walls.update({x+y*1j for x in range(int(start_x), int(end_x+1))})
    else:
        start_y = min(start_tile.imag, end_tile.imag)
        end_y = max(start_tile.imag, end_tile.imag)
        x = start_tile.real
        walls.update({x+y*1j for y in range(int(start_y), int(end_y+1))})
largest_x = max(coord.real for coord in red_tiles)
largest_y = max(coord.imag for coord in red_tiles)
smallest_x = min(coord.real for coord in red_tiles)
smallest_y = min(coord.imag for coord in red_tiles)

@cache
def is_interior(coord):
    if coord in walls: 
        return True
    tiles_east = {coord + x for x in range(int(largest_x - coord.real)+1)}
    tiles_north = {coord + y*1j for y in range(int(largest_y - coord.imag)+1)}
    tiles_south = {coord - x for x in range(int(coord.real)+1)}
    tiles_west = {coord - y*1j for y in range(int(coord.imag)+1)}
    if any(len(x & walls) == 0 for x in [tiles_east, tiles_north, tiles_south, tiles_west]):
        return False
    return True

# for testing
def print_tiles(to_highlight):
    for y in range(20):
        out = ""
        for x in range(20):
            if x+y*1j in to_highlight:
                out += "O"
            elif x+y*1j in walls:
                out += "X"
            else:
                out += "."
        print(out)

i = 0
def get_borders(corner_one, corner_two):
    x_range = range(int(max((corner_one.real, corner_two.real))) - int(min(corner_one.real, corner_two.real))+1)
    y_range = range(int(max((corner_one.imag, corner_two.imag))) - int(min(corner_one.imag, corner_two.imag))+1)
    return chain((min((corner_one, corner_two), key=lambda i: i.real) + x for x in x_range),
               (min((corner_one, corner_two), key=lambda i: i.imag) + y*1j for y in y_range),
               (max((corner_one, corner_two), key=lambda i: i.real) - x for x in x_range) ,
               (max((corner_one, corner_two), key=lambda i: i.imag) - y*1j for y in y_range) 
    )

def borders_interior(corner_one, corner_two):
    borders = get_borders(corner_one, corner_two)
    for border in borders:
        if not is_interior(border):
            return False
    return True
    
for area in sorted_areas:
    i += 1
    print(f"area {i}/{len(sorted_areas)}")
    corners = [area[0], 
               area[1], 
               area[0] + (area[1] - area[0]).real,
               area[0] + 1j*(area[1] - area[0]).imag]
    if all(is_interior(x) for x in corners):
        print(area[2])
        break