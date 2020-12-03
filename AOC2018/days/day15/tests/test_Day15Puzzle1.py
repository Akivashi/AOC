from unittest import TestCase
from Day15Puzzle1 import Day15Puzzle1

class Day15Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day15Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day15_test_input1.txt"), 2)
