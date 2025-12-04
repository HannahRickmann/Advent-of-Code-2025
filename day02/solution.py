# Advent of Code 2025 - Day 2
# Reads a list of id ranges from 'Day-2/input.txt'.
# The file is expected to contain a single line with comma-separated ranges,
# e.g. "1000-2000,3000-4000". Each range defines a start and end ID.

id_ranges = []

with open("day02/input.txt") as f:
    line= f.readline().strip().split(',')
    
for part in line:
    id_ranges.append(part.split('-'))

# ------------------ Part 1 ------------------
# Check the validity of each ID in the specified ranges
# An ID is considered valid if it does not contain a pair of identical halves.

resulting_sum = 0

def check_validity_1(id):  # Outputs True if the ID is valid, False otherwise
    id_str = str(id)

    if len(id_str) % 2 != 0:  # Check for odd length
        return True

    half_length = int(len(id_str) // 2)

    for pos in range(0, half_length):
        if id_str[pos] != id_str[pos + half_length]:  # Check if corresponding digits are equal
            return True
    return False

for id_range in id_ranges:
    start = int(id_range[0])
    end = int(id_range[1])
    for id in range(start, end + 1):
        if not check_validity_1(id):
            resulting_sum += id

print("Solution Day 2 - Part 1:", resulting_sum)


# ------------------ Part 2 ------------------
# Check the validity of each ID in the specified ranges
# An ID is considered valid if it does not contain any repeating patterns

resulting_sum = 0

def check_validity_2(id):  # Outputs True if the ID is valid, False otherwise
    id_str = str(id)
    is_valid = True

    max_pattern_length = len(id_str) // 2

    for pattern_length in range(1, max_pattern_length + 1):  # Check each possible pattern length
        if not is_valid:
            break

        pattern_occurs = True

        if len(id_str) % pattern_length != 0:  # Skip if the length is not a multiple of the pattern length
            pattern_occurs = False
        
        pos = 0
        while pos < (len(id_str) - pattern_length) and pattern_occurs and is_valid:
            if id_str[pos] != id_str[pos + pattern_length]:  # Check if corresponding digits are equal
                pattern_occurs = False
            pos += 1

        if pattern_occurs:
            is_valid = False

    return is_valid

for id_range in id_ranges:
    start = int(id_range[0])
    end = int(id_range[1])
    for id in range(start, end + 1):
        if not check_validity_2(id):
            resulting_sum += id

print("Solution Day 2 - Part 2:", resulting_sum)
