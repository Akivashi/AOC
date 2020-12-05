import argparse
import re

class Day5Puzzle2(object):
  def __init__(self):
    self.day = 5
    self.puzzle = 2

  def solution(self, inputfile):
    rowrule = re.compile("([FB]{7})([LR]{3})$")
    existing_seat_ids = []
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      seat_info = rowrule.search(line)
      row_binary = transform_row_to_binary(seat_info.group(1))
      column_binary = transform_column_to_binary(seat_info.group(2))
      existing_seat_ids.append(get_seat_id(row_binary, column_binary))
    
    existing_seat_ids.sort()

    prev_seat_id = existing_seat_ids[0]
    for seat_id in existing_seat_ids:
      if(seat_id != existing_seat_ids[0] and (seat_id-1) != prev_seat_id):
        return seat_id-1
      prev_seat_id = seat_id

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
  print(str(Day5Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
