# Advent of Code 2025 - Day 6
# Reads four lines of numbers and one line of operators from 'day06/input.txt'.
# Each number line contains space-separated integers.
# The operator line contains space-separated operators ('+' or '*').

# ------------------ Part 1 ------------------
# Read input data line by line and connect numbers based on the corresponding operator.

with open('day06/input.txt') as f:
    first_number = list(map(int, f.readline().strip().split()))
    second_number = list(map(int, f.readline().strip().split()))
    third_number = list(map(int, f.readline().strip().split()))
    fourth_number = list(map(int, f.readline().strip().split()))
    operator = f.readline().strip().split()

results = 0

for i in range(len(operator)):
    if operator[i] == '+':
        results += first_number[i] + second_number[i] + third_number[i] + fourth_number[i]
    elif operator[i] == '*':
        results += first_number[i] * second_number[i] * third_number[i] * fourth_number[i]

print("Solution Day 6 - Part 1:", results)


# ------------------ Part 2 ------------------
# The numbers are writtern vertically right-to-left in columns, and we need to read them as blocks based on the operators.

with open('day06/input.txt') as f:
    first_line = f.readline().rstrip("\n")
    second_line = f.readline().rstrip("\n")
    third_line = f.readline().rstrip("\n")
    fourth_line = f.readline().rstrip("\n")
    operator_line = f.readline().rstrip("\n")

def calculate_block(start_idx, end_idx):  # Calculates the result of a block of numbers from start_idx to end_idx based on the operator at start_idx
    numbers = []
    for idx in range(end_idx-2, start_idx - 1, -1):
        numbers.append(int(first_line[idx] + second_line[idx] + third_line[idx] + fourth_line[idx]))
    if operator_line[start_idx] == '+':
        return sum(numbers)
    elif operator_line[start_idx] == '*':
        result = 1
        for num in numbers:
            result *= num
        return result

current_idx = 0
results = 0

for idx, char in enumerate(operator_line[1:]):  # Iterate through operator line to find blocks
    if char != ' ':  # When we find the next operator, calculate the previous block
        results += calculate_block(current_idx, idx + 1)
        current_idx = idx + 1  # Store the start index of the next block
results += calculate_block(current_idx, len(operator_line)+1) # Calculate the last block

print("Solution Day 6 - Part 2:", results)
