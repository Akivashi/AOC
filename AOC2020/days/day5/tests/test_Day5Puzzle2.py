from unittest import TestCase
from Day5Puzzle2 import Day5Puzzle2

class Day5Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day5Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day5_test_input1.txt"), 2)
