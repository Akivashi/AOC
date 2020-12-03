import argparse

class Day1Puzzle1(object):
  def __init__(self):
    self.day = 1
    self.puzzle = 1

  def solution(self, inputfile):
    totalVal = 2020
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      lookup = str(totalVal-int(line))
      if search(lines, lookup):
        return int(line) * int(lookup)
    return "not found"

def search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return True
    return False

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day1Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
