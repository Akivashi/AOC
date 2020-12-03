import argparse

class Day8Puzzle1(object):
  def __init__(self):
    self.day = 8
    self.puzzle = 1

  def get_accumulated_meta_entries(self, code_line, current_accumulated_meta_data):
    nr_child_nodes = code_line[0]
    nr_metadata_entries = code_line[1]

    del code_line[0]
    del code_line[0]
    for child in range(0, nr_child_nodes):
      found = self.get_accumulated_meta_entries(code_line, current_accumulated_meta_data)
      current_accumulated_meta_data = found

    for i in range(0, nr_metadata_entries):
      current_accumulated_meta_data += code_line[0]
      del code_line[0]
    return current_accumulated_meta_data

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    code_line = [int(x) for x in  lines[0].split(" ")]
    return self.get_accumulated_meta_entries(code_line, 0)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day8Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
