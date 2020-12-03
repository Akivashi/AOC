from unittest import TestCase
from Day5Puzzle1 import Day5Puzzle1

class Day5Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day5Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day5_test_input1.txt"), 10)
