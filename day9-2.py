
from itertools import chain
from functools import cache
with open("test/day09.txt") as file:
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

# What I still need to do
# I found an algorithm for "AABB-AABBB 2D collision detection"
# Which lets you know if two rectangles collide *very* quickly
# Apparently it's useful but if it's only two rectangles that's a bit tough
# I think you treat each edge as a rectangle with length 1, effectively
# and if it doesn't intersect with any edges it's either completely inside or completely outside
# then you can just check if a random point is inside or outside
# Walls are part of the rectangle and also going to intersect, this might cause issues
# I think you replace the < > comparisons with <= >= and you're good
# walls need to be defined as start/end coordinates rather than a list of individual coordinates now

walls = []
walls = list(zip(red_tiles, red_tiles[1:] + [red_tiles[0]]))

def rect_intersects_wall(rectangle: list[complex]):
    rect_left = min(c.real for c in rectangle)
    rect_right = max(c.real for c in rectangle)
    rect_bottom = min(c.imag for c in rectangle)
    rect_top = max(c.imag for c in rectangle)
    for wall in walls:
        wall_left = min(c.real for c in wall)
        wall_right = max(c.real for c in wall)
        wall_bottom = min(c.imag for c in wall)
        wall_top = max(c.imag for c in wall)
        if not any([
            rect_left > wall_right, rect_right < wall_left, rect_bottom < wall_top, rect_top > wall_bottom
        ]):
            return True
    return False

for area in sorted_areas:
    if not rect_intersects_wall([area[0], area[1]]):
        print(area[2])
        break