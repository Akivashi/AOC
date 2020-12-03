import argparse

class Day8Puzzle2(object):
  def __init__(self):
    self.day = 8
    self.puzzle = 2

  def get_accumulated_meta_entries(self, code_line):
    nr_child_nodes = code_line[0]
    nr_metadata_entries = code_line[1]
    child_values = []
    my_value = 0
    del code_line[0]
    del code_line[0]
    for child in range(0, nr_child_nodes):
      found = self.get_accumulated_meta_entries(code_line)
      child_values.append(found)

    if nr_child_nodes == 0 :
      for i in range(0, nr_metadata_entries):
        my_value += code_line[i]
    else:
      for i in range(0, nr_metadata_entries):
        index = code_line[i]-1
        if code_line[i]-1 < len(child_values) and index >= 0:
          my_value += child_values[code_line[i]-1]  
    for i in range(0, nr_metadata_entries):
      del code_line[0]
    return my_value

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    code_line = [int(x) for x in  lines[0].split(" ")]
    return self.get_accumulated_meta_entries(code_line)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day8Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
