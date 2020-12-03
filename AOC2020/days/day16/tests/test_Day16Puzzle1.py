from unittest import TestCase
from Day16Puzzle1 import Day16Puzzle1

class Day16Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day16Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day16_test_input1.txt"), 2)
