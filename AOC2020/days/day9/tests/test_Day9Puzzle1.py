from unittest import TestCase
from Day9Puzzle1 import Day9Puzzle1

class Day9Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day9Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day9_test_input1.txt"), 2)
