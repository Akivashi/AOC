import argparse
import numpy as np
from Fabric import Fabric

class Day3Puzzle2(object):
  def __init__(self):
    self.day = 3
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    counter = 0
    fabric = np.zeros([1000, 1000], dtype=int)
    for line in lines:
      fabric_vars = Fabric(line)
      for x in range(0, fabric_vars.width):
        for y in range(0, fabric_vars.height):
          y_offset = fabric_vars.top+y
          fabric[fabric_vars.left+x][y_offset] += 1
          if(fabric[fabric_vars.left+x][y_offset] == 2):
            counter += 1
    
    for line in lines:
      fabric_vars = Fabric(line)
      intact = True
      for x in range(0, fabric_vars.width):
        for y in range(0, fabric_vars.height):
          if fabric[fabric_vars.left+x][fabric_vars.top+y] != 1:
            intact = False
      if intact:
        return fabric_vars.id
    return None

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day3Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
