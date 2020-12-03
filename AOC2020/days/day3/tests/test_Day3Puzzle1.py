from unittest import TestCase
from Day3Puzzle1 import Day3Puzzle1

class Day3Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day3Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day3_test_input1.txt"), 2)
