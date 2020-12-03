import argparse
import numpy as np
import copy

class Point(object):
  def __init__(self, line):
    point_information = line.split(",")
    self.x = int(point_information[0])
    self.y = int(point_information[1])
    self.velocity_x = int(point_information[2])
    self.velocity_y = int(point_information[3])

class Day10Puzzle1(object):
  def __init__(self):
    self.day = 10
    self.puzzle = 1

  def print_field(self, field):
    for line in field:
      print(line)

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    
    points = []
    for line in lines:
      line = line.replace("position=<", "").replace("velocity=<", ",").replace(">", "").replace(" ", "")
      points.append(Point(line))
    
    min_x = min(point.x for point in points)
    max_x = max(point.x for point in points)
    min_y = min(point.y for point in points)
    max_y = max(point.y for point in points)
    counter = 0

    while (max_x - min_x + max_y - min_y) > 100:
      counter += 1
      for point in points:
        insert_char = "#"
        if point.x == 9 and point.y == 1:
          insert_char = "X"
        new_index_x = point.x + abs(min_x) + point.velocity_x
        new_index_y = point.y + abs(min_y) + point.velocity_y
        point.x = point.x + point.velocity_x
        point.y = point.y + point.velocity_y
      min_x = min(point.x for point in points)
      max_x = max(point.x for point in points)
      min_y = min(point.y for point in points)
      max_y = max(point.y for point in points)

    size_x = abs(min_x) + abs(max_x) + 1
    size_y = abs(min_y) + abs(max_y) + 1

    empty_field = []
    for i in range (0, size_y):
      point_line = ""
      for j in range (0, size_x):
        point_line += "."
      empty_field.append(point_line)

    current_field = copy.deepcopy(empty_field)

    for point in points:
      insert_char = "#"
      if point.x == 9 and point.y == 1:
        insert_char = "X"
      index_x = point.x + abs(min_x)
      index_y = point.y + abs(min_y)
      line = current_field[index_y]
      line = line[:index_x] + insert_char + line[index_x + 1:]
      current_field[index_y] = line

    while True:
      input_key = input("Enter to continue, q + Enter to finish")
      if input_key == 'q':
        break
      counter += 1
      current_field = copy.deepcopy(empty_field)
      for point in points:
        insert_char = "#"
        if point.x == 9 and point.y == 1:
          insert_char = "X"
        new_index_x = point.x + abs(min_x) + point.velocity_x
        new_index_y = point.y + abs(min_y) + point.velocity_y
        line = current_field[new_index_y]
        line = line[:new_index_x] + insert_char + line[new_index_x + 1:]
        current_field[new_index_y] = line
        point.x = point.x + point.velocity_x
        point.y = point.y + point.velocity_y
      self.print_field(current_field)

    return counter

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day10Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
