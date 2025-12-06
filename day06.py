with open("input/day06.txt") as file:
    raw_lines = file.read().splitlines()
    no_whitespace_lines = [[x for x in y.split(" ")] for y in raw_lines]
    lines = [[x for x in y if x != ''] for y in no_whitespace_lines]

transpose = [[line[x] for line in lines] for x in range(len(lines[0]))]
equations = [line[-1].join(line[:-1]) for line in transpose]

# part 1
print(sum(eval(x) for x in equations))

char_transpose = [[line[x]
                   for line in raw_lines]
                  for x in range(len(raw_lines[0]))]

equations = []
operator = ""
current_numbers = []
for num_array in char_transpose:
    if num_array[-1] != " ":
        equations.append(operator.join(current_numbers[:-1]))
        operator = num_array[-1]
        current_numbers = []
    current_numbers.append("".join(num_array[:-1]))

equations.append(operator.join(current_numbers))

# part 2
print(sum(eval(x) for x in equations[1:]))
