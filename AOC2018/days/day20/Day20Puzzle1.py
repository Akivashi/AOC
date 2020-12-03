import argparse

class Day20Puzzle1(object):
  def __init__(self):
    self.day = 20
    self.puzzle = 1

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    for line in lines:
      print(line)
    return 2

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day20Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
