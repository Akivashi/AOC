from unittest import TestCase
from Day4Puzzle2 import Day4Puzzle2

class Day4Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day4Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day4_test_input1.txt"), 4455)
