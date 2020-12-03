from unittest import TestCase
from Day4Puzzle1 import Day4Puzzle1

class Day4Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day4Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day4_test_input1.txt"), 2)
