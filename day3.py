import sys

puzzle_input = open('day3.txt', 'r').read().split('\n')

example_input = '''
R8,U5,L5,D3
U7,R6,D4,L4
'''

directions = {
  'R': [1, 0],
  'U': [0, 1],
  'L': [-1, 0],
  'D': [0, -1]
}

def find_segment_pts(path, x, y):
  segment = []
  direction = path[0]
  distance = int(path[1:])
  for i in range(distance):
    x += directions[direction][0]
    y += directions[direction][1]
    segment.append([x, y])
  return segment

def store_all_pts(wire):
  x = 0
  y = 0
  points = []
  wire = wire.split(',')
  for path in wire:
    points += find_segment_pts(path, x, y)
  return points

def find_man_dist(point1, point2):
  return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def find_closest_intersection(wires):
  wire1 = store_all_pts(wires[0])
  wire2 = store_all_pts(wires[1])
  closest_x = 0
  closest_y = 0
  closest_man_dist = sys.maxint
  intersections = set(wire1) ^ set(wire2)
  for intersection in intersections:
    man_dist = find_man_dist([0, 0], [intersection])
    if man_dist < closest_man_dist:
      closest_x = intersection[0]
      closest_y = intersection[1]
      closest_man_dist = man_dist
  return closest_x, closest_y

print find_closest_intersection(example_input.strip().splitlines())
