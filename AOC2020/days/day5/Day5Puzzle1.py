import argparse

class Day5Puzzle1(object):
  def __init__(self):
    self.day = 5
    self.puzzle = 1

  def solution(self, inputfile):
    current_max_seat_id = 0
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      current_max_seat_id = max(
        current_max_seat_id,
        int(line
          .replace('F', '0')
          .replace('B', '1')
          .replace('L', '0')
          .replace('R', '1')
        , 2))
    return current_max_seat_id

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day5Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
