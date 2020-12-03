import argparse
import re

class Day2Puzzle2(object):
  def __init__(self):
    self.day = 2
    self.puzzle = 2

  def solution(self, inputfile):
    policy = re.compile("(\d*)-(\d*) ([a-z]): ([a-z]*)\n")
    valid_count = 0
    with open(inputfile,"r") as file:
      lines = file.readlines()
    for line in lines:
      g = policy.search(line)
      if g:
        lower = int(g.group(1))
        upper = int(g.group(2))
        letter = g.group(3)
        password = g.group(4)
        length = len(password)
        if ((length >= lower and length >= upper) and ((password[lower-1] == letter) ^ (password[upper-1] == letter))):
          valid_count += 1
    return valid_count

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day2Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
