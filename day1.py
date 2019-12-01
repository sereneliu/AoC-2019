puzzle_input = open('day1.txt', 'r').read().split('\n')

# Part 1

def find_fuel_required(mass):
	return mass//3 - 2
	
def find_total_fuel(modules):
	total = 0
	for module in modules:
		total += find_fuel_required(int(module))
	return total

# print find_total_fuel(puzzle_input) 
# Answer: 3212842

# Part 2

def find_fuel_for_fuel(fuel):
  total = 0
  while fuel > 0:
    fuel = find_fuel_required(fuel)
    if fuel > 0:
      total += fuel
  return total

def find_total_fuel2(modules):
  total = 0
  for module in modules:
		total += find_fuel_for_fuel(int(module))
  return total

print find_total_fuel2(puzzle_input)
# Answer: 4816402
