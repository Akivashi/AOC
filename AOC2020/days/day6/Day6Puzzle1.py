import argparse

class Day6Puzzle1(object):
  def __init__(self):
    self.day = 6
    self.puzzle = 1

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    lines.append('')
    unique_groupanswers = create_unique_groupanswers(lines)
    return len(''.join(unique_groupanswers))

def create_unique_groupanswers(lines):
  unique_groupanswers = []
  groupanswer_line = ''
  for n in range(len(lines)):
    line = lines[n].strip()
    if line == '':
      unique_groupanswers.append("".join(set(groupanswer_line)))
      groupanswer_line = ''
    else:
      groupanswer_line += line
  return unique_groupanswers

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day6Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
