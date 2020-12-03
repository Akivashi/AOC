from unittest import TestCase
from Day12Puzzle1 import Day12Puzzle1

class Day12Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day12Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day12_test_input1.txt"), 2)
