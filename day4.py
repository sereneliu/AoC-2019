puzzle_input = [372304, 847060]

def check_not_decreasing(number):
  str_number = str(number)
  for i in range(5):
    if not str_number[i] <= str_number[i + 1]:
      return False
  return True
  
def check_adjacent(number, check_larger_group):
  valid_adjacent = False
  str_number = str(number)
  for i in range(5):
    if not valid_adjacent:
      if str_number[i] == str_number[i + 1]:
        valid_adjacent = True
        if check_larger_group and valid_adjacent:
          if i != 0:
            if str_number[i] == str_number[i - 1]:
              valid_adjacent = False
          if i < 4:
            if str_number[i] == str_number[i + 2]:
              valid_adjacent = False
  return valid_adjacent

def check_valid_pw(number, check_larger_group):
  return check_not_decreasing(number) and check_adjacent(number, check_larger_group)
  
def find_valid_pws(start, end, check_larger_group):
  valid_pws = 0
  for number in range(start, end):
    if check_valid_pw(number, check_larger_group) == True:
      valid_pws += 1
  return valid_pws

# Part 1

# Key Facts:
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

print check_valid_pw(111111, False) # True
print check_valid_pw(223450, False) # False
print check_valid_pw(123789, False) # False

print find_valid_pws(puzzle_input[0], puzzle_input[1], False)
# Your puzzle answer was 475.

# Part 2

# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

print check_valid_pw(112233, True) # True
print check_valid_pw(123444, True) # False
print check_valid_pw(111122, True) # True

print find_valid_pws(puzzle_input[0], puzzle_input[1], True)
# Your puzzle answer was 297.
