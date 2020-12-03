from unittest import TestCase
from Day8Puzzle2 import Day8Puzzle2

class Day8Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day8Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day8_test_input1.txt"), 2)
