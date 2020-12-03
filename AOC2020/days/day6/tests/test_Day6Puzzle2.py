from unittest import TestCase
from Day6Puzzle2 import Day6Puzzle2

class Day6Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day6Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day6_test_input1.txt"), 2)
