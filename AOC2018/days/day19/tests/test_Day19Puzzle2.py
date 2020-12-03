from unittest import TestCase
from Day19Puzzle2 import Day19Puzzle2

class Day19Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day19Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day19_test_input1.txt"), 2)
