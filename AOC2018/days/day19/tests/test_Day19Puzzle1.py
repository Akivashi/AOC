from unittest import TestCase
from Day19Puzzle1 import Day19Puzzle1

class Day19Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day19Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day19_test_input1.txt"), 2)
