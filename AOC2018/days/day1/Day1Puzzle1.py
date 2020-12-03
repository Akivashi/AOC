import argparse

class Day1Puzzle1(object):
  def __init__(self):
    self.day = 1
    self.puzzle = 1
  
  def solution(inputfile):
    frequency = 0
    with open(inputfile,"r") as file:
      lines = file.readlines()
    for line in lines:
      frequency += int(line)
    return frequency

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--inputfile", required=True,
    help="frequency change input file", type=str)
  args = vars(ap.parse_args())
  print(str(Day1Puzzle1.solution(args["inputfile"])))

if __name__ == "__main__":
	main()