import sys

puzzle_input = open('day3.txt', 'r').read().split('\n')

# Part 1

example_input = '''
R8,U5,L5,D3
U7,R6,D4,L4
'''

example_input = example_input.strip().splitlines()

directions = {
  'R': [1, 0],
  'U': [0, 1],
  'L': [-1, 0],
  'D': [0, -1]
}

def find_segment_pts(path, x, y, steps):
  segment = {}
  direction = path[0]
  distance = int(path[1:])
  for i in range(distance):
    x += directions[direction][0]
    y += directions[direction][1]
    steps += 1
    if (x, y) not in segment.keys():
      segment[(x, y)] = steps
    else:
      segment[(x, y)].append(steps)
  return segment, x, y, steps

def store_all_pts(wire):
  x = 0
  y = 0
  steps = 0
  points = {}
  wire = wire.split(',')
  for path in wire:
    points.update(find_segment_pts(path, x, y, steps)[0])
    x = find_segment_pts(path, x, y, steps)[1]
    y = find_segment_pts(path, x, y, steps)[2]
    steps = find_segment_pts(path, x, y, steps)[3]
  return points

def find_man_dist(point1, point2):
  return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

# example_wire1 = store_all_pts(example_input[0])
# example_wire2 = store_all_pts(example_input[1])

puzzle_wire1 = store_all_pts(puzzle_input[0])
puzzle_wire2 = store_all_pts(puzzle_input[1])

def find_intersections(wire1, wire2):
  return set(wire1.keys()).intersection(set(wire2.keys()))

# example_intersections = find_intersections(example_wire1, example_wire2)
puzzle_intersections = find_intersections(puzzle_wire1, puzzle_wire2)

def find_closest_intersection(intersections):
  man_dist = sys.maxint
  for intersection in intersections:
    man_dist = min(man_dist, find_man_dist((0, 0), intersection))
  return man_dist

# print find_closest_intersection(example_intersections)
print find_closest_intersection(puzzle_intersections)
# Your puzzle answer was 2427.

# Part 2

def find_fewest_steps(intersections):
  fewest_steps = sys.maxint
  for intersection in intersections:
    steps = puzzle_wire1[intersection] + puzzle_wire2[intersection]
    fewest_steps = min(fewest_steps, steps)
  return fewest_steps

print find_fewest_steps(puzzle_intersections)
# Your puzzle answer was 27890.
