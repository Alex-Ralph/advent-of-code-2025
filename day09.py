from functools import cache
from line_profiler import profile
def main():
    with open("input/day09.txt") as file:
        red_tiles = [int(x[0]) + int(x[1])*1j for x in [y.split(",") for y in file.read().splitlines()]]
        
    areas = []
    for tile in red_tiles:
        tile_areas = [(tile, x, (abs((tile.real - x.real))+1) * (abs((tile.imag - x.imag))+1)) for x in red_tiles]
        areas += tile_areas
        
    sorted_areas = sorted(areas, key=lambda x: x[2], reverse=True)
    print(sorted_areas[0][2])

    @cache
    def wall_boundaries(wall: list[complex]):
        wall_left = min(c.real for c in wall)
        wall_right = max(c.real for c in wall)
        wall_bottom = min(c.imag for c in wall)
        wall_top = max(c.imag for c in wall)
        return (wall_left, wall_right, wall_bottom, wall_top)
    
    walls = list(zip(red_tiles, red_tiles[1:] + [red_tiles[0]]))
    @profile
    def rect_intersects_wall(rectangle: list[complex]):
        rect_left = min(c.real for c in rectangle)
        rect_right = max(c.real for c in rectangle)
        rect_bottom = min(c.imag for c in rectangle)
        rect_top = max(c.imag for c in rectangle)
        one_above = False
        one_below = False
        one_left = False
        one_right = False
        for wall in walls:
            wall_left, wall_right, wall_bottom, wall_top = wall_boundaries(wall)
            is_above = rect_top <= wall_bottom
            is_below = rect_bottom >= wall_top
            is_left = rect_right <= wall_left
            is_right = rect_left >= wall_right
            if not (is_above or is_below or is_left or is_right):
                return True
            one_above = one_above or is_above
            one_below = one_below or is_below
            one_left = one_left or is_left
            one_right = one_right or is_right
        if not (one_above and one_below and one_left and one_right):
            return True
        return False

    for area in sorted_areas:
        if not rect_intersects_wall([area[0], area[1]]):
            print(area[2])
            break

main()