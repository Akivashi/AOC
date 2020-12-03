from unittest import TestCase
from Day21Puzzle2 import Day21Puzzle2

class Day21Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day21Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day21_test_input1.txt"), 2)
