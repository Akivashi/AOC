from unittest import TestCase
from Day23Puzzle2 import Day23Puzzle2

class Day23Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day23Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day23_test_input1.txt"), 2)
