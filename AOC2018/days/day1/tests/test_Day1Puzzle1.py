from unittest import TestCase
from Day1Puzzle1 import Day1Puzzle1

class Day1Puzzle1Test(TestCase):

  def test_puzzle(self):
    self.assertEqual(Day1Puzzle1.solution("tests/Day1Puzzle1_test_input1.txt"), 3)
    self.assertEqual(Day1Puzzle1.solution("tests/Day1Puzzle1_test_input2.txt"), 0)
    self.assertEqual(Day1Puzzle1.solution("tests/Day1Puzzle1_test_input3.txt"), -6)