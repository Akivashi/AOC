from unittest import TestCase
from Day3Puzzle2 import Day3Puzzle2

class Day3Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day3Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day3_test_input1.txt"), 2)
