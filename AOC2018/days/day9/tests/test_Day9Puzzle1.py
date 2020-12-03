from unittest import TestCase
from Day9Puzzle1 import Day9Puzzle1

class Day9Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day9Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution("tests/Day9Puzzle1_test_input1.txt"), 8317)
    self.assertEqual(self.puzzle.solution("tests/Day9Puzzle1_test_input2.txt"), 146373)
    self.assertEqual(self.puzzle.solution("tests/Day9Puzzle1_test_input3.txt"), 2764)
    self.assertEqual(self.puzzle.solution("tests/Day9Puzzle1_test_input4.txt"), 54718)
    self.assertEqual(self.puzzle.solution("tests/Day9Puzzle1_test_input5.txt"), 37305)
