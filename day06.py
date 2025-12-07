from dataclasses import dataclass

with open("input/day06.txt") as file:
    raw_lines = file.read().splitlines()
    no_whitespace_lines = [[x for x in y.split(" ")] for y in raw_lines]
    lines = [[x for x in y if x != ''] for y in no_whitespace_lines]

transpose = [[line[x] for line in lines] for x in range(len(lines[0]))]


char_transpose = [[line[x]
                   for line in raw_lines]
                  for x in range(len(raw_lines[0]))]

equations = [line[-1].join(line[:-1]) for line in transpose]
# part 1
print(sum(eval(x) for x in equations))

operator_indices = [index for index, chars in enumerate(char_transpose) if chars[-1] != " "]

@dataclass
class Equation:
    operator: str
    operands: list[str]

# if an operator applies to all numbers between columns 15 and 20, this will contain a tuple (15, 20)
operator_ranges = zip(operator_indices, [x-1 for x in operator_indices[1:]] + [len(char_transpose)])

transposed_equations = [Equation(char_transpose[start_col][-1], 
                                [''.join(char_transpose[column][:-1]) for column in range(start_col, end_col)])
                        for start_col, end_col in operator_ranges]

equations = [
    eq.operator.join(eq.operands) for eq in transposed_equations
]
# part 2
print(sum(eval(x) for x in equations))