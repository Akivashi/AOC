from unittest import TestCase
from Day13Puzzle2 import Day13Puzzle2

class Day13Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day13Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day13_test_input1.txt"), 2)
