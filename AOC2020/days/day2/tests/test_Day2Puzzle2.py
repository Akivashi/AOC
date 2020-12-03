from unittest import TestCase
from Day2Puzzle2 import Day2Puzzle2

class Day2Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day2Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day2_test_input1.txt"), 2)
