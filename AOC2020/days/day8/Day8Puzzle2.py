import argparse
import re
import copy

class Instruction:
  def __init__(self, operation, change):
    self.operation = operation
    self.change = change
    self.visited = 0

  def __str__(self):
    return self.operation + " " + str(self.change) + " <> " + str(self.visited)

class Day8Puzzle2(object):
  def __init__(self):
    self.day = 8
    self.puzzle = 2

  def solution(self, inputfile):
    accumulator = 0
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    original_instructions = get_instructions(lines)

    for instruction_to_change in range(0, len(original_instructions)):
      if(original_instructions[instruction_to_change].operation == 'nop'):
        instructions = copy.deepcopy(original_instructions)
        instructions[instruction_to_change].operation = 'jmp'
        accumulator = find_accumulator(instructions)
        if(accumulator > 0):
          return accumulator
      elif(original_instructions[instruction_to_change].operation == 'jmp'):
        instructions = copy.deepcopy(original_instructions)
        instructions[instruction_to_change].operation = 'nop'
        accumulator = find_accumulator(instructions)
        if(accumulator > 0):
          return accumulator
    return 0

def find_accumulator(instructions):
  total_instructions = len(instructions)
  instruction_pointer = 0
  accumulator = 0
  while(instructions[instruction_pointer].visited == 0):
    if(instructions[instruction_pointer].operation == 'nop'):
      instructions[instruction_pointer].visited += 1
      instruction_pointer += 1
    elif(instructions[instruction_pointer].operation == 'acc'):
      instructions[instruction_pointer].visited += 1
      accumulator += instructions[instruction_pointer].change
      instruction_pointer += 1
    elif(instructions[instruction_pointer].operation == 'jmp'):
      instructions[instruction_pointer].visited += 1
      instruction_pointer += instructions[instruction_pointer].change
    if(instruction_pointer >= total_instructions):
      return accumulator
  return 0

def get_instructions(lines):
  instructions = []
  instruction_rule = re.compile("(.*) ([\+\-]\d*)")
  for line in lines:
    instruction = instruction_rule.search(line)
    instructions.append(Instruction(instruction.group(1), int(instruction.group(2))))
  return instructions

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day8Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
