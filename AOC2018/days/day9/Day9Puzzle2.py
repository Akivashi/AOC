import argparse
import numpy as np
from collections import deque

# original idea by Marcus Andrews
# https://reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/ebepyc7/

class Day9Puzzle2(object):
  def __init__(self):
    self.day = 9
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    words = lines[1].split(" ")
    players = int(words[0])
    total_marbles = int(words[6])
    scores = np.zeros(players, dtype=object)

    played_marbles = deque([0])

    for marble in range(1, total_marbles + 1):
        if marble % 23 == 0:
            played_marbles.rotate(7)
            scores[marble % players] += marble + played_marbles.pop()
            played_marbles.rotate(-1)
        else:
            played_marbles.rotate(-1)
            played_marbles.append(marble)

    return max(scores)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day9Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
