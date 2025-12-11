from itertools import combinations
from tqdm import tqdm

def pretty_print(list):
    for e in list:
        print(e)

boxes = []

with open("day08/input.txt") as f:
    for line in f:
        boxes.append(line.strip().split(","))

boxes = [tuple(map(int, box)) for box in boxes]


# ----------------- Part 1 ------------------

print("----------------- Part 1 ------------------")

def calculate_distance(box1, box2):
    return (box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2

def find_closest_boxes(distances):
    min_pair = min(distances, key=distances.get)
    min_distance = distances[min_pair]
    return min_pair, min_distance

def remove_closest_pair(distances, min_pair):
    distances.pop(min_pair)
    return distances

def include_box_in_circuits(min_pair, circuits):
    # Find which circuits (if any) contain the boxes
    circuits_with_boxes = [circuit for circuit in circuits if any(box in circuit for box in min_pair)]

    if len(circuits_with_boxes) == 0:
        # Case 1: Neither box is in any circuit → create new circuit
        circuits.append(list(min_pair))

    elif len(circuits_with_boxes) == 1:
        # Case 2: One box is in a circuit → add the missing box
        circuit = circuits_with_boxes[0]
        missing_box = [box for box in min_pair if box not in circuit]
        if len(missing_box) != 0:
            circuit.append(missing_box[0])
    
    elif len(circuits_with_boxes) == 2:
        # Case 3: Both boxes are in different circuits → merge circuits
        c1, c2 = circuits_with_boxes
        c1.extend(c2)       # add all boxes from c2 into c1
        circuits.remove(c2)  # remove the now-empty c2

    return circuits

distances = {
    pair: calculate_distance(pair[0], pair[1])
    for pair in combinations(boxes, 2)
}

circuits = []

for _ in tqdm(range(1000)):
    min_pair, min_distance = find_closest_boxes(distances)

    circuits = include_box_in_circuits(min_pair, circuits)

    # After handling, remove the pair from distances
    distances = remove_closest_pair(distances, min_pair)

    
# Sort lists by length in descending order and take the first three
top_circuits = sorted(circuits, key=len, reverse=True)[:3]

result = 1
for circuit in top_circuits:
    result *= len(circuit)

print("Product of sizes of top three circuits:", result)

print("----------------- Part 2 ------------------")

for _ in tqdm(range(len(distances))):
    min_pair, min_distance = find_closest_boxes(distances)

    circuits = include_box_in_circuits(min_pair, circuits)

    # After handling, remove the pair from distances
    distances = remove_closest_pair(distances, min_pair)

    if len(circuits) == 1 and len(circuits[0]) == len(boxes):
        break  # All boxes are in one circuit

print("Final connection:", min_pair)

"""
----------------- Part 1 ------------------
100%|█████████████████████████████████████████████████████████████████████| 1000/1000 [00:46<00:00, 21.58it/s]
Product of sizes of top three circuits: 153328
----------------- Part 2 ------------------
  1%|▌                                                                      | 4243/498500 [03:35<6:57:35, 19.73it/s]
Final connection: ((71430, 41887, 1462), (85337, 44242, 3891))
"""