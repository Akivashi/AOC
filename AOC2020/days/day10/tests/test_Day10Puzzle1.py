from unittest import TestCase
from Day10Puzzle1 import Day10Puzzle1

class Day10Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day10Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day10_test_input1.txt"), 2)
