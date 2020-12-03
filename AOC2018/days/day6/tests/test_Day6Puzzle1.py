from unittest import TestCase
from Day6Puzzle1 import Day6Puzzle1

class Day6Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day6Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day6_test_input1.txt"), 17)
