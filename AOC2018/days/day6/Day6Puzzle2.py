import argparse
import numpy as np

class Point(object):
  def __init__(self, coordinate):
    point = coordinate.split(', ')
    self.x = int(point[0])
    self.y = int(point[1])
    self.distance_to_closest = 0

  def manhattan_distance(self, point):
    return abs(self.x - point.x) + abs(self.y - point.y)

  def set_distance_to_closest(self, distance):
    self.distance_to_closest = distance

class Day6Puzzle2(object):
  def __init__(self):
    self.day = 6
    self.puzzle = 2

  def solution(self, inputfile, cutoff):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    coordinates = []
    for line in lines:
      coordinates.append(Point(line))
      
    field_x = max(point.x for point in coordinates)+1
    field_y = max(point.y for point in coordinates)+1
    
    field  = np.zeros([field_x, field_y])

    for x in range(0, field_x):
      for y in range(0, field_y):
        for point in coordinates:
          distance = point.manhattan_distance(Point(str(x) + ", " + str(y)))
          field[x][y] += distance

    total = 0
    for x in range(0, field_x):
      total += (field[x] < cutoff).sum()

    return total

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day6Puzzle2().solution(args["input"], 10000)))

if __name__ == "__main__":
  main()
