# Advent of Code 2025 - Day 4
# Reads a list of rows of rolls from 'day04/input.txt'.
# Each line is one row, where '.' indicates a free spot and '@' is a roll
# e.g. '..@@.@@@@.'

rows = []

with open("day04/input.txt") as f:
    for line in f:
        rows.append(list(line.strip()))

# ------------------ Part 1 ------------------
# Count rolls that are "accessible" — a roll '@' is accessible if it has fewer than 4 neighboring rolls ('@' or already-marked 'X')
# mark accessible rolls with 'X' and include them in the count

count_accessable_rolls = 0

max_row = len(rows)
max_col = len(rows[0])

for row_idx, row in enumerate(rows):
    for col_idx, roll in enumerate(row):
        count_adjacent_rolls = 0
        if roll == '.':
            continue

        adjacent_idx = [[row_idx-1, col_idx-1], [row_idx-1, col_idx], [row_idx-1, col_idx+1],
                        [row_idx, col_idx-1], [row_idx, col_idx+1],
                        [row_idx+1, col_idx-1], [row_idx+1, col_idx], [row_idx+1, col_idx+1]]

        for adj in adjacent_idx:
            if adj[0] < 0 or adj[0] >= max_row:
                continue
            if adj[1] < 0 or adj[1] >= max_col:
                continue
            if rows[adj[0]][adj[1]] == '@' or rows[adj[0]][adj[1]] == 'X':
                count_adjacent_rolls += 1

        if count_adjacent_rolls < 4:
            count_accessable_rolls += 1
            rows[row_idx][col_idx] = 'X'

print("Solution Day 4 -Part 1:", count_accessable_rolls)

# ------------------ Part 1 ------------------
# Count rolls that are "accessible" — a roll '@' is accessible if it has fewer than 4 neighboring rolls ('@' or already-marked 'X')
# This time we repeat the process untli no roll can be removed anymore

removed_rolls = 0

max_row = len(rows)
max_col = len(rows[0])

count_accessable_rolls = -1

while count_accessable_rolls != 0:
    count_accessable_rolls = 0
    for row_idx, row in enumerate(rows):
        for col_idx, roll in enumerate(row):
            count_adjacent_rolls = 0
            if roll == '.':
                continue

            adjacent_idx = [[row_idx-1, col_idx-1], [row_idx-1, col_idx], [row_idx-1, col_idx+1],
                            [row_idx, col_idx-1], [row_idx, col_idx+1],
                            [row_idx+1, col_idx-1], [row_idx+1, col_idx], [row_idx+1, col_idx+1]]

            for adj in adjacent_idx:
                if adj[0] < 0 or adj[0] >= max_row:
                    continue
                if adj[1] < 0 or adj[1] >= max_col:
                    continue
                if rows[adj[0]][adj[1]] == '@' or rows[adj[0]][adj[1]] == 'X':
                    count_adjacent_rolls += 1

            if count_adjacent_rolls < 4:
                count_accessable_rolls += 1
                rows[row_idx][col_idx] = 'X'
    rows = [['.' if roll == 'X' else roll for roll in row] for row in rows]
    removed_rolls += count_accessable_rolls

print("Solution Day 4 -Part 2:", removed_rolls)