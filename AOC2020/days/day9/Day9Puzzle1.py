import argparse

class Day9Puzzle1(object):
  def __init__(self):
    self.day = 9
    self.puzzle = 1

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    xmas_data = [int(i) for i in lines]

    lst = xmas_data[25:]
    preamble = xmas_data[:25]
    for target in lst:
      if(find_sum(preamble, target) != True):
        return target
      preamble.pop(0)
      preamble.append(target)
    return -1

def find_sum(preamble, target):
  for i in range(len(preamble)):
    preamble_1 = preamble[i]
    for preamble_2 in preamble[i:]:
      if((preamble_1 + preamble_2) == target):
        return True
  return False

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day9Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
