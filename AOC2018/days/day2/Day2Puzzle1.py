import argparse
from string import ascii_lowercase

class Day2Puzzle1(object):
  def __init__(self):
    self.day = 2
    self.puzzle = 1

  def hasGivenOccurences(line, number_of_occurences):
    for letter in ascii_lowercase :
      count = line.count(letter)
      if count == number_of_occurences:
        return True
    return False
  
  def solution(self, inputfile):
    occurence_two = 0
    occurence_three = 0
    with open(inputfile,"r") as file:
      lines = file.readlines()
    for line in lines :
      if Day2Puzzle1.hasGivenOccurences(line, 2):
        occurence_two += 1
      if Day2Puzzle1.hasGivenOccurences(line, 3):
        occurence_three += 1
    return occurence_two * occurence_three

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--inputfile", required=True,
    help="Box ID list input file", type=str)
  args = vars(ap.parse_args())

  print(str(Day2Puzzle1().solution(args["inputfile"])))

if __name__ == "__main__":
  main()
