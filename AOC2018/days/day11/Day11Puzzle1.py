import argparse
import numpy as np

class Day11Puzzle1(object):
  def __init__(self):
    self.day = 11
    self.puzzle = 1

  def get_powerlevel(self, x, y, serial_number):
    rack_id = x + 10
    powerlevel = rack_id * y
    powerlevel += serial_number
    powerlevel *= rack_id
    if powerlevel < 100:
      powerlevel = 0
    else:
      powerlevel = powerlevel % 1000
      if powerlevel > 99:
        powerlevel = int(str(powerlevel)[0])
      else:
        powerlevel = 0
    powerlevel -= 5
    return powerlevel

  def solution(self, serial_number):
    grid = np.zeros((300, 300), dtype=int)

    for x in range (0,300):
      for y in range (0,300):
        grid[x, y] = self.get_powerlevel(x+1, y+1, serial_number)
    
    winning_x = 0
    winning_y = 0
    max_fuel_cell_value = 0
    for x in range (0,298):
      for y in range (0,298):
        fuel_cell_value = 0
        for fuelcell_x in range(0,3):
          for fuelcell_y in range(0,3):
            fuel_cell_value += grid[x + fuelcell_x, y + fuelcell_y]
        if fuel_cell_value > max_fuel_cell_value:
          max_fuel_cell_value = fuel_cell_value
          winning_x = x+1
          winning_y = y+1

    return str(winning_x) + "," + str(winning_y)

def main():
  print(str(Day11Puzzle1().solution(3214)))

if __name__ == "__main__":
  main()
