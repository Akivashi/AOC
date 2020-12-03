import argparse
import string
import networkx as nx
import matplotlib.pyplot as plt

class Day7Puzzle1(object):
  def __init__(self):
    self.day = 7
    self.puzzle = 1

  # draw function to visualize the problem
  def show_step_by_step_graph(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    G = nx.DiGraph()
    for line in lines:
      words = line.split(' ')
      G.add_edge(words[1],words[7])
    nx.draw(G, with_labels = True, pos=nx.circular_layout(G))
    plt.show()

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()

    assembly_lines = []
    for line in lines:
      words = line.split(' ')
      assembly_lines.append((words[1]+words[7]))

    assembly_order = ""
    start_nodes = []

    for char_step1 in string.ascii_uppercase:
      first_steps = [ order for order in assembly_lines if order[0]  == char_step1 ]
      second_steps = [ order for order in assembly_lines if order[1]  == char_step1 ]
      if not second_steps and first_steps:
        for step in first_steps:
          if step[0] not in start_nodes:
            start_nodes.append(step[0])

    while start_nodes:
      start_nodes = sorted(start_nodes) # keep entry nodes in alphabetical order
      node = start_nodes[0]
      del start_nodes[0]
      assembly_order = assembly_order + node
      to_remove = []
      for line in assembly_lines:
        if line[0] == node:
          to_remove.append(line)
          second_steps = [ from_to for from_to in assembly_lines if from_to[1] == line[1] ]
          if len(second_steps) == 1:
            start_nodes.append(line[1])
      for remove in to_remove:
        assembly_lines.remove(remove)
    return assembly_order

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day7Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
