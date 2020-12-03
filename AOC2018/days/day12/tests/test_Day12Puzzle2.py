from unittest import TestCase
from Day12Puzzle2 import Day12Puzzle2

class Day12Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day12Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day12_test_input1.txt"), 2)
