import argparse

class Day1Puzzle2(object):
  def __init__(self):
    self.day = 1
    self.puzzle = 2
  
  def solution(inputfile):
    frequency = 0
    previous_frequencies = set([frequency])
    with open(inputfile,"r") as file:
      lines = file.readlines()
    frequency_repeated = False
    while not frequency_repeated:
      for line in lines:
        frequency += int(line)
        if frequency in previous_frequencies:
          frequency_repeated = True
          return frequency
        previous_frequencies.add(frequency)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--inputfile", required=True,
    help="frequency change input file", type=str)
  args = vars(ap.parse_args())
  print(str(Day1Puzzle2.solution(args["inputfile"])))

if __name__ == "__main__":
	main()