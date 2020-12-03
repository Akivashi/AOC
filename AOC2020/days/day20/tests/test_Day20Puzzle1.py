from unittest import TestCase
from Day20Puzzle1 import Day20Puzzle1

class Day20Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day20Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day20_test_input1.txt"), 2)
