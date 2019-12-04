puzzle_input = [372304, 847060]

# Part 1

# Key Facts:
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

def check_valid_pw(number):
  adjacent = False
  str_number = str(number)
  for i in range(5):
    if not str_number[i] <= str_number[i + 1]:
      return False
    if not adjacent:
      if str_number[i] == str_number[i + 1]:
        adjacent = True
  return adjacent
  
def find_valid_pws(start, end):
  valid_pws = 0
  for number in range(start, end):
    if check_valid_pw(number) == True:
      valid_pws += 1
  return valid_pws

# print check_valid_pw(111111) # True
# print check_valid_pw(223450) # False
# print check_valid_pw(123789) # False

# print find_valid_pws(puzzle_input[0], puzzle_input[1])
# Your puzzle answer was 475.

# Part 2

# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

def check_adjacent(number):
  one_after = False
  str_number = str(number)
  for i in range(5):
    if not one_after:
      if str_number[i] == str_number[i + 1]:
        one_after = True
        if one_after:
          if i != 0:
            if str_number[i] == str_number[i - 1]:
              one_after = False
          if i < 4:
            if str_number[i] == str_number[i + 2]:
              one_after = False
  return one_after

def check_valid_pw2(number):
  adjacent = False
  str_number = str(number)
  for i in range(5):
    if not str_number[i] <= str_number[i + 1]:
      return False
    if not adjacent:
      if check_adjacent(number):
        adjacent = True
  return adjacent

def find_valid_pws2(start, end):
  valid_pws = 0
  for number in range(start, end):
    if check_valid_pw2(number) == True:
      valid_pws += 1
  return valid_pws

# print check_adjacent(112233) # True
# print check_adjacent(123444) # False
# print check_adjacent(111122) # True

print find_valid_pws2(puzzle_input[0], puzzle_input[1])
# Your puzzle answer was 297.
