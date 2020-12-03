from unittest import TestCase
from Day15Puzzle2 import Day15Puzzle2

class Day15Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day15Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day15_test_input1.txt"), 2)
