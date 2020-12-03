from unittest import TestCase
from Day25Puzzle2 import Day25Puzzle2

class Day25Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day25Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day25_test_input1.txt"), 2)
