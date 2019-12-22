import intcode

puzzle_input = open('day2.txt', 'r').read().split(',')

# Part 1

def convert_to_int(string_input):
  return [int(n) for n in string_input]

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
      if intcode.intcode(restore(test_program, n, v), 0) == output:
        return 100 * n + v
      else:
        test_program = convert_to_int(gravity_assist)

print find_inputs(puzzle_input, 19690720)
# Your puzzle answer was 5335.
