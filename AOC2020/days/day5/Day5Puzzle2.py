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
      row_input = seat_info.group(1)
      column_input = seat_info.group(2)
      existing_seat_ids.append(get_row(row_input) * 8 + get_column(column_input))
    existing_seat_ids.sort()

    prev_seat_id = existing_seat_ids[0]
    for seat_id in existing_seat_ids:
      if(seat_id != existing_seat_ids[0] and (seat_id-1) != prev_seat_id):
        return seat_id-1
      prev_seat_id = seat_id

def get_row(row_input):
  row_nr = 0
  if(row_input[0] == 'B'):
    row_nr+=64
  if(row_input[1] == 'B'):
    row_nr+=32
  if(row_input[2] == 'B'):
    row_nr+=16
  if(row_input[3] == 'B'):
    row_nr+=8
  if(row_input[4] == 'B'):
    row_nr+=4
  if(row_input[5] == 'B'):
    row_nr+=2
  if(row_input[6] == 'B'):
    row_nr+=1
  return row_nr

def get_column(column_input):
  column_nr = 0
  if(column_input[0] == 'R'):
    column_nr+=4
  if(column_input[1] == 'R'):
    column_nr+=2
  if(column_input[2] == 'R'):
    column_nr+=1
  return column_nr

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day5Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
