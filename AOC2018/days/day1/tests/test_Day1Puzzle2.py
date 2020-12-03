from unittest import TestCase
from Day1Puzzle2 import Day1Puzzle2

class Day1Puzzle2Test(TestCase):

  def test_puzzle(self):
    self.assertEqual(Day1Puzzle2.solution("tests/Day1Puzzle2_test_input1.txt"), 0)
    self.assertEqual(Day1Puzzle2.solution("tests/Day1Puzzle2_test_input2.txt"), 10)
    self.assertEqual(Day1Puzzle2.solution("tests/Day1Puzzle2_test_input3.txt"), 5)
    self.assertEqual(Day1Puzzle2.solution("tests/Day1Puzzle2_test_input4.txt"), 14)