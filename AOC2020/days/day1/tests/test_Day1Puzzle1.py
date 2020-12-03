from unittest import TestCase
from Day1Puzzle1 import Day1Puzzle1

class Day1Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day1Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day1_test_input1.txt"), 2)
