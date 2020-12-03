from unittest import TestCase
from Day11Puzzle1 import Day11Puzzle1

class Day11Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day11Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day11_test_input1.txt"), 2)
