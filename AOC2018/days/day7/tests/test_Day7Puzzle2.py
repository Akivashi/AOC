from unittest import TestCase
from Day7Puzzle2 import Day7Puzzle2

class Day7Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day7Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day7_test_input1.txt"), 253)
