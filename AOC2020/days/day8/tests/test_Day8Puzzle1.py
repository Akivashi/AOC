from unittest import TestCase
from Day8Puzzle1 import Day8Puzzle1

class Day8Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day8Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day8_test_input1.txt"), 2)
