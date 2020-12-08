import argparse
import re
from collections import defaultdict

class Day7Puzzle2(object):
  def __init__(self):
    self.day = 7
    self.puzzle = 2

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
        if(vertex.group(1) == 'no'):
          addEdge(graph, node, "0 " + vertex.group(2))
        else:
          addEdge(graph, node, vertex.group(1) + " " + vertex.group(2))

    return getBagsInColor(graph, 'shiny gold') - 1 # remove the golden bag

def addEdge(graph,u,v):
  graph[u].append(v)

def getBagsInColor(graph, color):
  bag_information_rule = re.compile("(\d*) (.*)")
  bag_types = graph[color]
  count = 1
  for bag_type in bag_types:
    bag_info = bag_information_rule.search(bag_type)
    bag_count = int(bag_info.group(1))
    bag_color = bag_info.group(2)
    if(bag_count == 0):
      return 1
    else:
      bags_inside = getBagsInColor(graph, bag_color)

      count += bag_count * bags_inside
  return count


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day7Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
