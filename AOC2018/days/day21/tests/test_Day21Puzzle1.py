from unittest import TestCase
from Day21Puzzle1 import Day21Puzzle1

class Day21Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day21Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day21_test_input1.txt"), 2)
