from unittest import TestCase
from Day7Puzzle1 import Day7Puzzle1

class Day7Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day7Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day7_test_input1.txt"), 2)
