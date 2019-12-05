puzzle_input = open('day2.txt', 'r').read().split(',')

# Part 1

example_input = [1,9,10,3,2,3,11,0,99,30,40,50]

def convert_to_int(string_input):
  return [int(n) for n in string_input]

def intcode(gravity_assist):
  p0 = 0
  p1 = 1
  p2 = 2
  p3 = 3
  opcode = gravity_assist[p0]
  while opcode != 99:
    input1 = gravity_assist[p1]
    input2 = gravity_assist[p2]
    output = gravity_assist[p3]
    if opcode == 1:
      gravity_assist[output] = gravity_assist[input1] + gravity_assist[input2]
    if opcode == 2:
      gravity_assist[output] = gravity_assist[input1] * gravity_assist[input2]
    p0 += 4
    p1 += 4
    p2 += 4
    p3 += 4
    opcode = gravity_assist[p0]
  return gravity_assist[0]

def restore(gravity_assist, noun, verb):
  gravity_assist[1] = noun
  gravity_assist[2] = verb
  return gravity_assist

# print intcode(restore(puzzle_input, 12, 2))
# Your puzzle answer was 4930687.

# Part 2

def find_inputs(gravity_assist, output):
  initial_program = gravity_assist
  test_program = convert_to_int(gravity_assist)
  for n in range(100):
    for v in range(100):
      if intcode(restore(test_program, n, v)) == output:
        return 100 * n + v
      else:
        test_program = convert_to_int(gravity_assist)

print find_inputs(puzzle_input, 19690720)
# Your puzzle answer was 5335.
