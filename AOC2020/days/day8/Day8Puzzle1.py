import argparse
import re

class Instruction:
  def __init__(self, operation, change):
    self.operation = operation
    self.change = change
    self.visited = 0

  def __str__(self):
    return self.operation + " " + str(self.change) + " <> " + str(self.visited)

class Day8Puzzle1(object):
  def __init__(self):
    self.day = 8
    self.puzzle = 1

  def solution(self, inputfile):
    accumulator = 0
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    instructions = get_instructions(lines)
    instruction_pointer = 0
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
    return accumulator

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
  print(str(Day8Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
