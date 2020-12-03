import argparse

class Day2Puzzle2(object):
  def __init__(self):
    self.day = 2
    self.puzzle = 2

  def compare_ids(line1, line2):
    matched_index = -1
    for index, (char_line1, char_line2) in enumerate(zip(line1, line2)):
      if char_line1 != char_line2:
        if matched_index != -1:
          return None
        else:
          matched_index = index
    if matched_index >= 0:
      return line1[:matched_index] + line1[matched_index+1:]
    return None

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    for line_index in range(0, len(lines)):
      line1 = lines[line_index].rstrip()
      for line2_index in range(line_index+1, len(lines)):
        line2 = lines[line2_index].rstrip()
        result = Day2Puzzle2.compare_ids(line1, line2)
        if result != None:
          return result
    return None

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--inputfile", required=True,
    help="Box ID list input file", type=str)
  args = vars(ap.parse_args())
  print(str(Day2Puzzle2().solution(args["inputfile"])))

if __name__ == "__main__":
  main()
