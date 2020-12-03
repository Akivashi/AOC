from unittest import TestCase
from Day9Puzzle2 import Day9Puzzle2

class Day9Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day9Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day9_test_input1.txt"), 2)
