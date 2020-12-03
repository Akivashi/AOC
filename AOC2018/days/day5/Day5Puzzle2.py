import argparse
import string
import operator

class Day5Puzzle2(object):
  def __init__(self):
    self.day = 5
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    return self.breakdown_polymer(lines[0])

  def breakdown_polymer(self, original_polymer):
    reactions = []
    remove_reactions = {}
    for letter in string.ascii_lowercase:
      remove_reactions.update( {letter : 0 })
      reactions.append(letter + letter.upper())
      reactions.append(letter.upper() + letter)

    for key in remove_reactions.keys():
      polymer = original_polymer.replace(key, "")
      polymer = polymer.replace(key.upper(), "")
      polymer_stable = False

      while(polymer_stable != True):
        polymer_stable = True
        for reaction in reactions:
          oldlen = len(polymer)
          polymer = polymer.replace(reaction, "")
          if oldlen != len(polymer):
            polymer_stable = False
      count = len(polymer)
      remove_reactions.update( {key : count })
    return min(remove_reactions.items(), key=operator.itemgetter(1))[1]

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day5Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
