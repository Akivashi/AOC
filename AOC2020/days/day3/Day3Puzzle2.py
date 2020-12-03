import argparse
from functools import reduce

class Day3Puzzle2(object):
  def __init__(self):
    self.day = 3
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    tree_count_results = [
       count_trees_for_slope(lines, 1, 1),
       count_trees_for_slope(lines, 3, 1),
       count_trees_for_slope(lines, 5, 1),
       count_trees_for_slope(lines, 7, 1),
       count_trees_for_slope(lines, 1, 2)
    ]
    print(tree_count_results)
    return reduce((lambda x, y: x * y), tree_count_results)

def count_trees_for_slope(lines, x_offset, y_offset):
  tree_count = 0
  for n in range(0, int(len(lines)/y_offset)):
    line = lines[n*y_offset]
    if line[n*x_offset % len(line)] == '#':
      tree_count += 1
  return tree_count

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day3Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
