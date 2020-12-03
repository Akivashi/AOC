from unittest import TestCase
from Day24Puzzle2 import Day24Puzzle2

class Day24Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day24Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day24_test_input1.txt"), 2)
