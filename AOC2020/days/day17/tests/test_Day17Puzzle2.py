from unittest import TestCase
from Day17Puzzle2 import Day17Puzzle2

class Day17Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day17Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day17_test_input1.txt"), 2)
