import argparse

class Day5Puzzle2(object):
  def __init__(self):
    self.day = 5
    self.puzzle = 2

  def solution(self, inputfile):
    existing_seat_ids = []
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      existing_seat_ids.append(
        int(line
              .replace('F', '0')
              .replace('B', '1')
              .replace('L', '0')
              .replace('R', '1')
            , 2))
    
    existing_seat_ids.sort()

    prev_seat_id = existing_seat_ids[0]
    for seat_id in existing_seat_ids:
      if(seat_id != existing_seat_ids[0] and (seat_id-1) != prev_seat_id):
        return seat_id-1
      prev_seat_id = seat_id

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day5Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
