import argparse
import re

class Day2Puzzle1(object):
  def __init__(self):
    self.day = 2
    self.puzzle = 1

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
        letter_count = password.count(letter)
        if letter_count >= lower and letter_count <= upper:
          valid_count += 1
    return valid_count

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day2Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
