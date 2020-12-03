import argparse
import string
import operator

class Day7Puzzle2(object):
  def __init__(self):
    self.day = 7
    self.puzzle = 2

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()

    assembly_lines = []
    for line in lines:
      words = line.split(' ')
      assembly_lines.append((words[1]+words[7]))

    start_nodes = []

    for char_step1 in string.ascii_uppercase:
      first_steps = [ order for order in assembly_lines if order[0]  == char_step1 ]
      second_steps = [ order for order in assembly_lines if order[1]  == char_step1 ]
      if not second_steps and first_steps:
        for step in first_steps:
          add = True
          for node in start_nodes:
            if step[0] == node[0]:
              add = False
          if add:
            start_nodes.append((step[0],61+ord(step[0])-ord('A'), -1))

    seconds_spend = 0

    workers = [False,False,False,False,False]

    while start_nodes:
      start_nodes_to_remove = []
      # put workers to work
      for start_node_index in range(0,len(start_nodes)):
        start_node = start_nodes[start_node_index]
        if start_node[1] != 0 and start_node[2] == -1:
          for worker_index in range(0,len(workers)):
            worker = workers[worker_index]
            if worker == False:
              workers[worker_index] = True
              start_nodes[start_node_index] = (start_node[0], start_node[1], worker_index)
              break # node assigned, so break to not double assign work


      # perform least amount of work
      least_work_seconds = 0
      try:
        least_work_seconds = min(seconds for (step, seconds, worker) in start_nodes if worker > -1)
      except ValueError:
        continue

      for start_node_index in range(0,len(start_nodes)):
        start_node = start_nodes[start_node_index]
        if start_node[2] > -1:
          start_nodes[start_node_index] = (start_node[0], start_node[1] - least_work_seconds, start_node[2])
      seconds_spend += least_work_seconds

      # remove workers if they are finished
      for start_node_index in range(0,len(start_nodes)):
        start_node = start_nodes[start_node_index]
        if start_node[1] == 0:
          workers[start_node[2]] = False
          start_nodes[start_node_index] = (start_node[0], 0, -1)
          start_nodes_to_remove.append(start_node_index)

      to_remove = []
      for node_index in start_nodes_to_remove:
        node = start_nodes[node_index]
        del start_nodes[node_index]
        for line in assembly_lines:
          if line[0] == node[0]:
            to_remove.append(line)
            second_steps = [ from_to for from_to in assembly_lines if from_to[1] == line[1]]
            if len(second_steps) == 1:
              start_nodes.append((line[1],61+ord(line[1])-ord('A'), -1))

      for remove in to_remove:
        assembly_lines.remove(remove)

    return seconds_spend

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day7Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
