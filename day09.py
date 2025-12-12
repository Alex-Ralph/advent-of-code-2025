from itertools import combinations
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

# draw the walls
# for each vertex in each rectangle, check it's inside by "drawing" a beam north and east
# each beam should cross a boundary an odd number of times

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

# def get_coords_in_square(first_corner, second_corner):
#     return {x+y*1j 
#             for x in range(
#                 int(min(first_corner.real, second_corner.real)), int(max(first_corner.real, second_corner.real)+1))
#             for y in range(
#                 int(min(first_corner.imag, second_corner.imag)), int(max(first_corner.imag, second_corner.imag)+1))
#             }

def all_coords_interior(first_corner, second_corner):
    for x in range(int(min(first_corner.real, second_corner.real)), int(max(first_corner.real, second_corner.real)+1)):
        for y in range(int(min(first_corner.imag, second_corner.imag)), int(max(first_corner.imag, second_corner.imag)+1)):
            if not is_interior(x+y*1j):
                return False
    return True

largest_x = max(coord.real for coord in red_tiles)
largest_y = max(coord.imag for coord in red_tiles)

@cache
def is_interior(coord):
    if coord in walls: 
        return True
    tiles_east = {coord + x for x in range(int(largest_x - coord.real)+1)}
    tiles_north = {coord + y*1j for y in range(int(largest_y - coord.imag)+1)}
    if len(tiles_north & walls) % 2 != 1 or (len(tiles_north) == 1 and coord in walls):
        return False
    if len(tiles_east & walls) % 2 != 1 or (len(tiles_east) == 1 and coord in walls):
        return False
    return True

# for testing
# def print_tiles(to_highlight):
#     for y in range(20):
#         out = ""
#         for x in range(20):
#             if x+y*1j in to_highlight:
#                 out += "O"
#             elif x+y*1j in walls:
#                 out += "X"
#             else:
#                 out += "."
#         print(out)

i = 0
for area in sorted_areas:
    i += 1
    print(f"area {i}/{len(sorted_areas)}")
    if all_coords_interior(area[0], area[1]):
        print(area[2])
        break