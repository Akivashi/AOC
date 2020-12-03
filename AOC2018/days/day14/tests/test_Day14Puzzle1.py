from unittest import TestCase
from Day14Puzzle1 import Day14Puzzle1

class Day14Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day14Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day14_test_input1.txt"), 2)
