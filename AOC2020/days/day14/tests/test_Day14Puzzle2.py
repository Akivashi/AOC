from unittest import TestCase
from Day14Puzzle2 import Day14Puzzle2

class Day14Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day14Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day14_test_input1.txt"), 2)
