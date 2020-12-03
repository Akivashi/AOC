from unittest import TestCase
from Day2Puzzle1 import Day2Puzzle1

class Day2Puzzle1Test(TestCase):
  def setUp(self):
    self.puzzle = Day2Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day2Puzzle1_test_input1.txt"), 12)
