import argparse

class Day9Puzzle2(object):
  def __init__(self):
    self.day = 9
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    xmas_data = [int(i) for i in lines]
    target = 127

    for index_start in range(0, len(xmas_data)):
      for index_end in range(1, len(xmas_data)):
        contiguous_set = xmas_data[index_start:index_end]
        if(sum(contiguous_set) == target):
          return(min(contiguous_set) + max(contiguous_set))

    return -1

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day9Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
