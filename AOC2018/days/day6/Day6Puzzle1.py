import argparse

class Point(object):
  def __init__(self, coordinate):
    point = coordinate.split(', ')
    self.x = int(point[0])
    self.y = int(point[1])
    self.distance_to_closest = None
    self.closest = None
    self.same_distance = False
  
  def manhattan_distance(self, point):
    return abs(self.x - point.x) + abs(self.y - point.y)

  def set_closest(self, point):
    self.closest = point

  def set_same_distance(self, same):
    self.same_distance = same

  def set_distance_to_closest(self, distance):
    self.distance_to_closest = distance

class Day6Puzzle1(object):
  def __init__(self):
    self.day = 6
    self.puzzle = 1

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    coordinates = []
    for line in lines:
      coordinates.append(Point(line))

    field_x = max(point.x for point in coordinates)+1
    field_y = max(point.y for point in coordinates)+1

    field  = [[Point(str(x) + ", " + str(y)) for y in range(field_y)] for x in range(field_x)]

    for x in range(0, field_x):
      for y in range(0, field_y):
        for point in coordinates:
          distance = point.manhattan_distance(field[x][y])
          if field[x][y].distance_to_closest == None:
            field[x][y].set_distance_to_closest(distance)
            field[x][y].set_closest(point)
            field[x][y].set_same_distance(False)
          elif distance == field[x][y].distance_to_closest:
            field[x][y].set_same_distance(True)
          elif distance < field[x][y].distance_to_closest:
            field[x][y].set_distance_to_closest(distance)
            field[x][y].set_closest(point)
            field[x][y].set_same_distance(False)

    point_area = []
    edgepoints = set()
    edge_x = field_x-1
    edge_y = field_y-1
    
    for point_index in range(0, len(coordinates)):
      my_area = 0
      point = coordinates[point_index]
      for x in range(0, field_x):
        for y in range(0, field_y):
          if x == 0 or y == 0 or x == edge_x or y == edge_y:
            edgepoints.add(str(field[x][y].closest.x) + ", " + str(field[x][y].closest.y))
          if field[x][y].same_distance == False and field[x][y].closest != None:
            if field[x][y].closest.x == point.x and field[x][y].closest.y == point.y:
              my_area +=1
      if str(point.x) + ", " + str(point.y) in edgepoints:
        point_area.append(0)
      else:
        point_area.append(my_area)

    return max(point_area)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day6Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
