from unittest import TestCase
from Day17Puzzle1 import Day17Puzzle1

class Day17Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day17Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day17_test_input1.txt"), 2)
