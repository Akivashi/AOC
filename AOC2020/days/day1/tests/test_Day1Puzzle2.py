from unittest import TestCase
from Day1Puzzle2 import Day1Puzzle2

class Day1Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day1Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day1_test_input1.txt"), 2)
