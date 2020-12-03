from unittest import TestCase
from Day11Puzzle2 import Day11Puzzle2

class Day11Puzzle2Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day11Puzzle2()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.solution(18), "90,269,16")
    self.assertEqual(self.puzzle.solution(42), "232,251,12")
