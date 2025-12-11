# Advent of Code 2025 - Day 7
# Reads a manifold layout from 'day07/input.txt'.
# The manifold contains:
# 'S' - start point of the beam
# '^' - a splitter that splits the beam into two paths
# '.' - empty space

manifold = []

with open("day07/input.txt") as f:
    for line in f:
        manifold.append(list(line.strip()))

def pretty_print(manifold):
    for row in manifold:
        print("".join(f"{str(x):>3}" for x in row))
    print()

# ------------------ Part 1 ------------------
# Count how many splitters ('^') the beam encounters as it travels from 'S' to the bottom of the manifold.
# The beam starts at 'S' and moves downwards, splitting into two paths at each splitter.

def find_start(manifold):
    return manifold[0].index("S")

def set_beam_path(manifold,row,splitter_pos): # set beam path in given row at given splitter position
    manifold[row][splitter_pos-1] = '|'
    manifold[row][splitter_pos+1] = '|'
    return manifold

manifold[1][find_start(manifold)] = '|'
counter = 0

for row in range(1, len(manifold) - 1):
    for idx, char in enumerate(manifold[row]):
        if char == '|':
            if manifold[row+1][idx] == '^':
                counter += 1
                set_beam_path(manifold, row+1, idx)
            else:
                manifold[row+1][idx] = '|'

print("Solution Day 7 - Part 1:", counter)

# ------------------ Part 2 ------------------
# Count how many different paths the beam can take to reach the bottom of the manifold.

manifold = [
    [0 if x == '.' or x == '|' else x for x in row]
    for row in manifold
]

def set_beam_path_with_cardinality(manifold, row, splitter_pos, char): # set beam path in given row at given splitter position, char is the character before splitting
    manifold[row][splitter_pos-1] += char  # propagate the number of paths to the left
    manifold[row][splitter_pos+1] += char  # propagate the number of paths to the right
    return manifold

manifold[1][find_start(manifold)] = 1  # start with one path at the starting position

for row in range(1, len(manifold) - 1):
    for idx, char in enumerate(manifold[row]):
        if type(char) == int and char > 0:  # if there are paths at this position
            if manifold[row+1][idx] == '^':  # splitter encountered
                set_beam_path_with_cardinality(manifold, row+1, idx, char)
            else:
                manifold[row+1][idx] += char  # propagate the number of paths downwards if there is no splitter

print("Solution Day 7 - Part 2:", sum(manifold[-1]))  # sum all paths that reached the bottom row