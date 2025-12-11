# Advent of Code 2025 - Day 5
# Reads a list of turn instructions from 'day05/input.txt'.
# WE have two sections in the input file, separated by a blank line.
# The first section contains ID ranges, and the second section contains available IDs.
# e.g. "1-5" in the first section and "3" in the second section.

id_ranges = []
available_ids = []

with open("day05/input.txt", "r", encoding="utf-8") as f:
    before_blank = True
    for line in f:
        line = line.strip()
        
        # Detect blank line separating the two sections
        if line == "":
            before_blank = False
            continue

        # If we are still in the first section, parse ID ranges
        if before_blank:
            id_ranges.append([int(part) for part in line.split('-')])
        else:  # In the second section, parse available IDs
            available_ids.append(int(line))

# ------------------ Part 1 ------------------
# Determine how many available IDs fall within any of the given ID ranges.

def is_id_fresh(id, id_ranges):  # Outputs True if id is within any of the ranges
    for start, end in id_ranges:
        if start <= id <= end:
            return True
    return False

fresh_ids = []
for id in available_ids:
    if is_id_fresh(id, id_ranges):
        fresh_ids.append(id)

print("Solution Day 5 - Part 1:", len(fresh_ids))

# ------------------ Part 2 ------------------
# Determine how many unique IDs are covered by the given ID ranges.

"""
# naive but slow solution: build a set of all IDs in the ranges

fresh_ids_set = set()

for start, end in id_ranges:
    for id in range(start, end + 1):
        fresh_ids_set.add(id)
"""

# efficient solution

merged_ranges = []
for start, end in id_ranges:
    overlapping_ranges = []
    for ref_start, ref_end in merged_ranges:  # check if reference range overlaps with current range
        if ref_start <= start <= ref_end:
            overlapping_ranges.append([ref_start, ref_end])
        elif ref_start <= end <= ref_end:
            overlapping_ranges.append([ref_start, ref_end])
        elif start <= ref_start and end >= ref_end:
            overlapping_ranges.append([ref_start, ref_end])

    if len(overlapping_ranges) == 0:  # no overlaps, just add the range
        merged_ranges.append([start,end])
        continue
    
    # merge all overlapping ranges with the current range
    min_start = min([r[0] for r in overlapping_ranges] + [start])
    max_end = max([r[1] for r in overlapping_ranges] + [end])
    for r in overlapping_ranges:
        merged_ranges.remove(r)
    merged_ranges.append([min_start, max_end])
    

total_fresh_ids = sum(r[1] - r[0] + 1 for r in merged_ranges)
print("Solution Day 5 - Part 2:", total_fresh_ids)
