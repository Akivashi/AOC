from unittest import TestCase
from Day24Puzzle1 import Day24Puzzle1

class Day24Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day24Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day24_test_input1.txt"), 2)
