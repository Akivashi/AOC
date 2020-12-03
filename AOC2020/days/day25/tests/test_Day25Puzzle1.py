from unittest import TestCase
from Day25Puzzle1 import Day25Puzzle1

class Day25Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day25Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day25_test_input1.txt"), 2)
