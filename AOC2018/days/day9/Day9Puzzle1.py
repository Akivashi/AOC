import argparse
import numpy as np

class Day9Puzzle1(object):
  def __init__(self):
    self.day = 9
    self.puzzle = 1

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    words = lines[0].split(" ")
    players = int(words[0])
    total_marbles = int(words[6])
    scores = np.zeros(players, dtype=int)

    played_marbles = [0]

    current_marble = 0
    for marble in range(1, total_marbles+1):
      if marble % 23 == 0:
        current_marble = current_marble - 7
        if current_marble < 0:
          current_marble = len(played_marbles) + current_marble
        value = played_marbles[current_marble] + marble
        del played_marbles[current_marble]
        scores[marble % players] += value
      else:
        if len(played_marbles) == 1:
          played_marbles.append(marble)
          current_marble = 1
        else:
          current_marble +=2
          if len(played_marbles) == current_marble:
            played_marbles.append(marble)
          else:
            if len(played_marbles) < current_marble:
              current_marble = current_marble % (len(played_marbles))
            played_marbles.insert(current_marble, marble)

    return max(scores)

def main():
  # ap = argparse.ArgumentParser()
  # ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  # args = vars(ap.parse_args())
  # print(str(Day9Puzzle1().solution(args["input"])))
  print(str(Day9Puzzle1().solution("c:/Projects/AOC2018/days/day9/input.txt")))

if __name__ == "__main__":
  main()
