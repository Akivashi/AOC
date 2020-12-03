from unittest import TestCase
from Day22Puzzle1 import Day22Puzzle1

class Day22Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day22Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day22_test_input1.txt"), 2)
