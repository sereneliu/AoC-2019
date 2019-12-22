def intcode(program, i):
  o = []
  p = 0
  opcode = program[p]
  while opcode != 99:
    if opcode == 1:
      program[program[p + 3]] = program[program[p + 1]] + program[program[p + 2]]
    elif opcode == 2:
      program[program[p + 3]] = program[program[p + 1]] * program[program[p + 2]]
    elif opcode == 3:
      program[program[p + 1]] = i
    elif opcode == 4:
      o.append(program[program[p + 1]])
    p += 4
    opcode = program[p]
  return program[0]
