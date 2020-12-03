import argparse

class Day3Puzzle1(object):
  def __init__(self):
    self.day = 3
    self.puzzle = 1

  def solution(self, inputfile):
    tree_count = 0
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for n in range(len(lines)):
      line = lines[n]
      if line[n*3 % len(line)] == '#':
        tree_count += 1
    return tree_count

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day3Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
