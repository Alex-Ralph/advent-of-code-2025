with open("input/day07.txt") as file:
    manifold = [list(x) for x in file.read().splitlines()]
    
emitter = manifold[0].index("S")
manifold[1][emitter] = 1
manifold = [[0 if x == "." else x for x in line] for line in manifold]

splits = 0
quantum_splits = 0
for i, line in enumerate(manifold[2:]):
    row = i+2
    for col, digit in enumerate(line):
        above = manifold[row-1][col]
        if type(above) == int and above > 0:
            if type(digit) == int:
                manifold[row][col] += manifold[row-1][col]
            elif digit == "^":
                new_split = False
                if type(manifold[row][col-1]) == int:
                    manifold[row][col-1] += above
                    new_split = True

                if type(manifold[row][col+1]) == int:
                    manifold[row][col+1] += above
                    new_split = True
                if new_split == True:
                    splits += 1

print(splits)
print(sum(manifold[-1]))
    
