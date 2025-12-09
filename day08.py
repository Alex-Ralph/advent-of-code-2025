from math import prod
EDGE_COUNT = 1000
with open("input/day08.txt") as file:
    coordinates = [tuple((int(x) for x in line.split(","))) for line in file.read().splitlines()]

edges = []
for index, coord in enumerate(coordinates):
    for second_coord in coordinates[index+1:]:
        edges.append([coord, second_coord, (
                    (coord[0] - second_coord[0]) ** 2 +
                    (coord[1] - second_coord[1]) ** 2 + 
                    (coord[2] - second_coord[2]) ** 2)])

edges.sort(key=lambda x: x[2])
shortest_edges = [[x[0], x[1]] for x in edges[:EDGE_COUNT]]
subgraphs = []

for coord in coordinates:
    connected_edges = [y for y in shortest_edges if coord in y]
    connected_vertices = [x for y in connected_edges for x in y if x != coord]
    connected_subgraphs = [sg for sg in subgraphs if any(v in sg for v in connected_vertices)]
    if connected_subgraphs == 0:
        subgraphs.append[[coord]]
        continue
    new_subgraph = list(set([x for y in connected_subgraphs for x in y]))
    new_subgraph.append(coord)
    for subgraph in connected_subgraphs:
        subgraphs.remove(subgraph)
    subgraphs.append(new_subgraph)

print(prod(sorted([len(x) for x in subgraphs], reverse=True)[:3]))


subgraphs = [[x] for x in coordinates]
all_edges = [[x[0], x[1]] for x in edges]

for edge in all_edges:
    subgraphs_to_merge = [sg for sg in subgraphs if edge[0] in sg or edge[1] in sg]
    subgraphs.append([x for y in subgraphs_to_merge for x in y])
    for sg in subgraphs_to_merge:
        subgraphs.remove(sg)
    if len(subgraphs) == 1:
        print(edge[0][0] * edge[1][0])
        break