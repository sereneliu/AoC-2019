puzzle_input = open('day12.txt', 'r').read().split('\n')

def apply_gravity(pos1, pos2, vel1, vel2):
  if pos1 > pos2:
    vel1 -= 1
  elif pos1 < pos2:
    vel1 += 1
  return vel1

def update_velocity(moon1, moon2):
  for i in range(3):
    moon1.vel[i] = apply_gravity(moon1.pos[i], moon2.pos[i], moon1.vel[i], moon2.vel[i])
  return moon1, moon2
    
def update_position(moon):
  for i in range(3):
    moon.pos[i] += moon.vel[i]
  return moon

def update_all_velocities(moons):
  for moon1 in moons:
    for moon2 in moons:
      if moon1 != moon2:
        moon1, moon2 = update_velocity(moon1, moon2)
  return moons

def update_all_positions(moons):
  for moon in moons:
    moon = update_position(moon)
  return moons
  
def take_time_steps(moons, steps):
  for i in range(steps):
    update_all_velocities(moons)
    update_all_positions(moons)
  return moons

class Moon:
  def __init__(self, x, y, z):
    self.pos = [x, y, z]
    self.vel = [0, 0, 0]

def create_moon(position):
  x = int(position[position.index('x=') + 2:position.index('y=') - 2])
  y = int(position[position.index('y=') + 2:position.index('z=') - 2])
  z = int(position[position.index('z=') + 2:position.index('>')])
  return Moon(x, y, z)

def create_moons(positions):
  moon1 = create_moon(positions[0])
  moon2 = create_moon(positions[1])
  moon3 = create_moon(positions[2])
  moon4 = create_moon(positions[3])
  return moon1, moon2, moon3, moon4

moons = create_moons(puzzle_input)

def calc_energy(x, y, z):
  return abs(x) + abs(y) + abs(z)

def calc_total_energy(pot, kin):
  return pot * kin

def calc_sum(moons):
  total = 0
  for moon in moons:
    total += calc_total_energy(calc_energy(moon.pos[0], moon.pos[1], moon.pos[2]), calc_energy(moon.vel[0], moon.vel[1], moon.vel[2]))
  return total

print calc_sum(take_time_steps(moons, 1000))
