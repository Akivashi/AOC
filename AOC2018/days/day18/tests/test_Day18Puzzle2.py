from unittest import TestCase
from Day18Puzzle2 import Day18Puzzle2

class Day18Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day18Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day18_test_input1.txt"), 2)
