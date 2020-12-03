from unittest import TestCase
from Day20Puzzle2 import Day20Puzzle2

class Day20Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day20Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day20_test_input1.txt"), 2)
