from unittest import TestCase
from Day10Puzzle2 import Day10Puzzle2

class Day10Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day10Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day10_test_input1.txt"), 2)
