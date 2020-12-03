from unittest import TestCase
from Day22Puzzle2 import Day22Puzzle2

class Day22Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day22Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day22_test_input1.txt"), 2)
