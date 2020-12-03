import argparse
import string

class Day5Puzzle1(object):
  def __init__(self):
    self.day = 5
    self.puzzle = 1
    
  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    polymer = lines[0]
    polymer_stable = False

    reactions = []
    for letter in string.ascii_lowercase:
      reactions.append(letter + letter.upper())
      reactions.append(letter.upper() + letter)

    while(polymer_stable != True):
      polymer_stable = True
      for reaction in reactions:
        oldlen = len(polymer)
        polymer = polymer.replace(reaction, "")
        if oldlen != len(polymer):
          polymer_stable = False
    return len(polymer)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day5Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
