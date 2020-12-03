from unittest import TestCase
from Day23Puzzle1 import Day23Puzzle1

class Day23Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day23Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day23_test_input1.txt"), 2)
