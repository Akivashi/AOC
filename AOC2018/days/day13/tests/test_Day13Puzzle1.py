from unittest import TestCase
from Day13Puzzle1 import Day13Puzzle1

class Day13Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day13Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day13_test_input1.txt"), 2)
