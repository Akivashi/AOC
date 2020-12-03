from unittest import TestCase
from Day18Puzzle1 import Day18Puzzle1

class Day18Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day18Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day18_test_input1.txt"), 2)
