import argparse

class Day6Puzzle2(object):
  def __init__(self):
    self.day = 6
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    lines.append('')
    groupanswers = create_groupanswers(lines)
    return count_same_answers(groupanswers)

def create_groupanswers(lines):
  groupanswers = []
  groupanswer_line = []
  for n in range(len(lines)):
    line = lines[n].strip()
    if line == '':
      groupanswers.append(groupanswer_line)
      groupanswer_line = []
    else:
      groupanswer_line.append(line)
  return groupanswers

def count_same_answers(groupanswers):
  same_answers_count = 0
  for answers in groupanswers:
    group_size = len(answers)
    same_answer_count = 0
    for char in "".join(set("".join(answers))):
      if(group_size == len([answer for answer in answers if char in answer])):
        same_answer_count +=1
    same_answers_count += same_answer_count
  return same_answers_count

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day6Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
