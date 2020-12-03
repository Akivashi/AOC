import argparse
from shutil import copyfile
import os

def mkdir(folder):
  if not os.path.exists(folder):
    try:
      os.makedirs(os.path.dirname(folder))
    except OSError as exc: # Guard against race condition
      return

def intialize_files(location):
  fileExtension = ".py"
  initFile = "__init__.py"

  for day in range(1, 26):
    day_str = str(day)
    
    top_folder = location + "/days/"
    puzzles_folder = top_folder + "day" + day_str + "/"
    test_folder = puzzles_folder + "/tests/"
    
    mkdir(top_folder)
    mkdir(puzzles_folder)
    mkdir(test_folder)

    for puzzle in range(1, 3):
      puzzle_str = str(puzzle)
      class_name = "Day" + day_str + "Puzzle" + puzzle_str
      filepath = puzzles_folder + class_name + fileExtension
      test_filepath = test_folder + "test_" + class_name + fileExtension
      
      if not os.path.exists(filepath):
        with open(filepath,"w+") as file:
          file.write("import argparse\n")
          file.write("\n")
          file.write("class " + class_name + "(object):\n")
          file.write("  def __init__(self):\n")
          file.write("    self.day = " + day_str + "\n")
          file.write("    self.puzzle = " + puzzle_str + "\n")
          file.write("\n")
          file.write("  def solution(self, inputfile):\n")
          file.write("    with open(inputfile,\"r\") as file:\n")
          file.write("      lines = file.read.splitlines()\n")
          file.write("    for line in lines:\n")
          file.write("      print(line)\n")
          file.write("    return 2\n")
          file.write("\n")
          file.write("def main():\n")
          file.write("  ap = argparse.ArgumentParser()\n")
          file.write("  ap.add_argument(\"-i\", \"--input\", required=True, help=\"input value\", type=str)\n")
          file.write("  args = vars(ap.parse_args())\n")
          file.write("  print(str(" + class_name + "().solution(args[\"input\"])))\n")
          file.write("\n")
          file.write("if __name__ == \"__main__\":\n")
          file.write("  main()\n")

        with open(puzzles_folder + initFile,"w+") as file:
          file.write("# this makes sure the directory is seen as a module")
      
        with open(puzzles_folder + "input.txt","w+") as file:
          file.write("# inputfile")
    
      if not os.path.exists(test_filepath):
        test_input_filename = "Day" + day_str + "_test_input1.txt"
        with open(test_filepath,"w+") as file:
          file.write("from unittest import TestCase\n")
          file.write("from " + class_name + " import " + class_name + "\n")
          file.write("\n")
          file.write("class " + class_name + "Test(TestCase):\n")
          file.write("  \n")
          file.write("  def setUp(self):\n")
          file.write("    self.puzzle = " + class_name + "()\n")
          file.write("  \n")
          file.write("  def test_puzzle(self):\n")
          file.write("    self.assertEqual(self.puzzle.solution(\"tests/" + test_input_filename + "\"), 2)\n")

        with open(test_folder + initFile,"w+") as file:
          file.write("# this makes sure the directory is seen as a module")

        with open(test_folder + test_input_filename,"w+") as file:
          file.write("# test input file")

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-location", "--location", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  location = args["location"]
  mkdir(location)
  intialize_files(location)

if __name__ == "__main__":
  main()