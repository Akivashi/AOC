from unittest import TestCase
from Day16Puzzle2 import Day16Puzzle2

class Day16Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day16Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day16_test_input1.txt"), 2)
