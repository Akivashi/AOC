import argparse

class Day1Puzzle2(object):
  def __init__(self):
    self.day = 1
    self.puzzle = 2

  def solution(self, inputfile):
    totalVal = 2020
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      for line2 in lines:
        if line != line2:
          lookup = str(totalVal-int(line)-int(line2))
          if search(lines, lookup):
            print(line + " ; " + line2 + " ; " + lookup)
            return int(line) * int(line2) * int(lookup)

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
  print(str(Day1Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
