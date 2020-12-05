import argparse
import re

class Day5Puzzle1(object):
  def __init__(self):
    self.day = 5
    self.puzzle = 1

  def solution(self, inputfile):
    rowrule = re.compile("([FB]{7})([LR]{3})$")
    current_max_seat_id = 0
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      seat_info = rowrule.search(line)
      row_binary = transform_row_to_binary(seat_info.group(1))
      column_binary = transform_column_to_binary(seat_info.group(2))
      current_max_seat_id = max(current_max_seat_id, get_seat_id(row_binary, column_binary))
    return current_max_seat_id

def transform_row_to_binary(row_input):
  return row_input.replace('F', '0').replace('B', '1')

def transform_column_to_binary(column_input):
  return column_input.replace('L', '0').replace('R', '1')

def get_seat_id(row_binary, column_binary):
  return int(row_binary, 2) * 8 + int(column_binary, 2)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day5Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
