# Advent of Code 2025 - Day 3
# Reads a list of battery banks from 'Day-3/input.txt'.
# Each bank is represented as a string of digits.

banks = []

with open("day03/input.txt") as f:
    for line in f:
        banks.append(line.strip()) 

# ------------------ Part 1 ------------------
# For each bank, find the two highest digits and combine them to form a two-digit number.
# We cannot rearrange the batteries, so the second highest digit must come after the highest digit.
# Sum these two-digit numbers for all banks to get the final output.

output_joltage = 0

for bank in banks:
    first_digit = bank[0]  # Find the highest digit
    first_digit_idx = 0
    for idx, battery in enumerate(bank):
        if idx == len(bank) - 1:
            break
        if int(battery) > int(first_digit):
            first_digit = int(battery)
            first_digit_idx = idx
        if first_digit == 9:
            break

    second_digit = int(bank[first_digit_idx + 1])  # Find the second highest digit after the highest digit
    second_digit_idx = first_digit_idx + 1
    for idx in range(first_digit_idx + 1, len(bank)):
        battery = bank[idx]
        if int(battery) > second_digit:
            second_digit = int(battery)
            second_digit_idx = idx
        if second_digit == 9:
            break

    output_joltage += int(str(first_digit) + str(second_digit))

print("Solution Day 3 - Part 1:", output_joltage)

# ------------------ Part 2 ------------------
# For each bank, find the twelve highest digits and combine them to form a twelve-digit number
# We cannot rearrange the batteries, so each digit must come after the previous one.
# Sum these twelve-digit numbers for all banks to get the final output.

output_joltage = 0

for bank in banks: 
    selected_digits = []
    start_idx = 0

    for digit_idx in range(12):  # Find each of the twelve digits
        current_digit = bank[start_idx]
        current_digit_idx = start_idx

        for idx in range(start_idx, len(bank) - (12 - digit_idx) + 1):  # Ensure enough digits remain
            battery = bank[idx]
            if int(battery) > int(current_digit):  # Found a new higher digit
                current_digit = battery
                current_digit_idx = idx
            if current_digit == '9':
                break
        selected_digits.append(str(current_digit))
        start_idx = current_digit_idx + 1

    output_joltage += int(''.join(selected_digits))

print("Solution Day 3 - Part 2:", output_joltage)