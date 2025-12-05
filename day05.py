with open("input/day05.txt") as file:
    rangelist, ingredients_list = [x.splitlines() for x in file.read().split("\n\n")]

fresh_id_ranges = [[int(x[0]), int(x[1])] for x in [y.split("-") for y in rangelist]]
ingredient_ids = (int(x) for x in ingredients_list)

sorted_id_ranges = sorted(fresh_id_ranges, key=lambda x: x[0])

def remove_overlap(id_ranges: list[tuple[int]]) -> list[tuple[int]]:
    for index, id_range in enumerate(id_ranges[:-1]):
        if id_range[1] > id_ranges[index+1][1]:
            id_ranges[index+1][1] = id_range[1]
        if id_range[1] >= id_ranges[index+1][0]:
            id_range[1] = id_ranges[index+1][0] - 1
    return [x for x in id_ranges if x[0] <= x[1]]

no_overlap_ranges = remove_overlap(sorted_id_ranges)

fresh_ingredient_count = sum([
    1 for x in ingredient_ids
    if any(x >= id_range[0] and x <= id_range[1] for id_range in no_overlap_ranges)
])

fresh_ingredient_ids = sum(
    (id_range[1] - id_range[0]) + 1 
    for id_range in no_overlap_ranges)

print(fresh_ingredient_count)
print(fresh_ingredient_ids)
