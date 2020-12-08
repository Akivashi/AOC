import argparse
import re
from collections import defaultdict

class Day7Puzzle1(object):
  def __init__(self):
    self.day = 7
    self.puzzle = 1

  def solution(self, inputfile):
    graph = defaultdict(list)
    contain_rule = re.compile("(.*) bags? (contain )((\d*|no) .* bags?)*.")
    connection_rule = re.compile("(\d*|no) (.*) bags?")
    with open(inputfile,"r") as file:
      lines = file.read().splitlines()
    for line in lines:
      bag_connections = contain_rule.search(line)
      node = bag_connections.group(1)
      for bag_connection in bag_connections.group(3).split(', '):
        vertex = connection_rule.search(bag_connection)
        if(vertex.group(1) != 'no'):
          addEdge(graph, node, vertex.group(2))

    curr_colors = {el:False for el in graph}
    curr_colors['shiny gold'] = True
    county = 0
    while(getParentsOfCurrColors(graph, curr_colors) and county < 100):
      county+=1
      continue

    ways = 0
    for key, value in curr_colors.items():
      if(value == True):
        ways+=1
    return ways-1 # remove the shiny gold bag as an option

def addEdge(graph,u,v):
  graph[u].append(v)

def getParentsOfCurrColors(graph, curr_colors):
  changeMade = False
  newDict = dict()
  for (key, value) in curr_colors.items():
   # Check if key is even then add pair to new dictionary
   if value:
    newDict[key] = value
  for color in newDict.keys():
    for node, childs in graph.items():
      if(color in childs and curr_colors[node] == False):
        curr_colors[node] = True
        changeMade = True
  return changeMade

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day7Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
