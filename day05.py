
print("starting")
with open("input/day05.txt") as file:
    rangelist, ingredients_list = [x.splitlines() for x in file.read().split("\n\n")]

fresh_id_ranges = [(int(x[0]), int(x[1])) for x in [y.split("-") for y in rangelist]]
ingredient_ids = (int(x) for x in ingredients_list)

sorted_id_ranges = sorted(fresh_id_ranges, key=lambda x: x[0])

def reduce_id_ranges(id_ranges: list[tuple[int]]) -> list[tuple[int]]:
    if len(id_ranges) == 0:
        return []
    highest_in_first_range = id_ranges[0][1]
    reduced_list = []
    for id_range in id_ranges[1:]:
        if id_range[1] <= highest_in_first_range:
            continue
        if id_range[0] <= highest_in_first_range:
            reduced_list.append((highest_in_first_range+1, id_range[1]))
            continue
        reduced_list.append(id_range)
    return [(id_ranges[0])] + [x for x in reduce_id_ranges(reduced_list)]

reduced_fresh_id_ranges = reduce_id_ranges(sorted_id_ranges)

fresh_ingredients = [
    x for x in ingredient_ids
    if any(x >= id_range[0] and x <= id_range[1] for id_range in reduced_fresh_id_ranges)
]

fresh_ingredient_count = sum(
    (id_range[1] - id_range[0]) + 1 
    for id_range in reduced_fresh_id_ranges)

print(len(fresh_ingredients))
print(fresh_ingredient_count)
