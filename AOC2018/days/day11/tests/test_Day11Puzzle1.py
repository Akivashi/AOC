from unittest import TestCase
from Day11Puzzle1 import Day11Puzzle1

class Day11Puzzle1Test(TestCase):
  
  def setUp(self):
    self.puzzle = Day11Puzzle1()
  
  def test_puzzle(self):
    self.assertEqual(self.puzzle.get_powerlevel(122, 79, 57), -5)
    self.assertEqual(self.puzzle.get_powerlevel(217, 196, 39), 0)
    self.assertEqual(self.puzzle.get_powerlevel(101, 153, 71), 4)
    self.assertEqual(self.puzzle.solution(18), "33,45")
    self.assertEqual(self.puzzle.solution(42), "21,61")
