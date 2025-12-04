# Advent of Code 2025 - Day 1
# Reads a list of turn instructions from 'Day-1/input.txt'.
# Each line is expected to be a direction letter ('L' or 'R') followed by an integer,
# e.g. "L10" or "R3". The rest of the file simulates movement on a circular track.

numbers = []

with open("day01/input.txt") as f:
    for line in f:
        numbers.append(line.strip())  

# ------------------ Part 1 ------------------
# Calculate how many times the position wraps around ending on zero on a circular track of size 100.

position = 50  # Starting position on circular track
zero_counter = 0
positions = [position]

for number in numbers:
    direction = number[0]      
    value = int(number[1:])

    if direction == "L":
        position -= value
        position %= 100
    elif direction == "R":
        position += value
        position %= 100
    else:
        raise ValueError("Invalid direction")
    positions.append(position)

    if position == 0:
        zero_counter += 1

print("Solution Day 1 - Part 1:", zero_counter)

# ------------------ Part 2 ------------------
# Calculate how many times the position wraps around crossing zero on a circular track of size 100


position = 50  # Starting position on circular track
prev_position = position  # necessary for special case to not double count zeroes
zero_counter = 0
positions = [position]

for number in numbers:
    direction = number[0]      
    value = int(number[1:])

    if direction == "L":
        if prev_position == 0:  # special case: when we start at zero and go to the left, we should not double count
            zero_counter -= 1
        position -= value
        zero_counter += ((position - 1) // 100) * -1
    elif direction == "R":
        position += value
        zero_counter += position // 100
    else:
        raise ValueError("Invalid direction")
    
    position %= 100
    
    prev_position = position
    positions.append(position)

print("Solution Day 1 - Part 2:", zero_counter)
