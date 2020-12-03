from unittest import TestCase
from Day11Puzzle2 import Day11Puzzle2

class Day11Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day11Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day11_test_input1.txt"), 2)
