import argparse
import numpy as np
import threading

class Day11Puzzle2(object):
  def __init__(self):
    self.day = 11
    self.puzzle = 2
    self.winning_grid_x = 0
    self.winning_grid_y = 0
    self.winning_grid = 0
    self.max_grid_fuel_cell_value = 0
    self.lock = threading.Lock()
    self.threads = []

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

  def get_max_fuel_cell_of_size(self, grid, size):
    winning_x = 0
    winning_y = 0
    max_fuel_cell_value = 0
    for x in range (0,300-size+1):
      for y in range (0,300-size+1):
        fuel_cell_value = 0
        for fuelcell_x in range(0, size):
          for fuelcell_y in range(0, size):
            fuel_cell_value += grid[x + fuelcell_x, y + fuelcell_y]
        if fuel_cell_value > max_fuel_cell_value:
          max_fuel_cell_value = fuel_cell_value
          winning_x = x+1
          winning_y = y+1
    self.lock.acquire()
    if max_fuel_cell_value > self.max_grid_fuel_cell_value:
        self.winning_grid_x = winning_x
        self.winning_grid_y = winning_y
        self.winning_grid = size
        self.max_grid_fuel_cell_value = max_fuel_cell_value
    self.lock.release()
    return

  def solution(self, serial_number):
    grid = np.zeros((300, 300), dtype=int)

    for x in range (0,300):
      for y in range (0,300):
        grid[x, y] = self.get_powerlevel(x+1, y+1, serial_number)
    
    for size in range(0,300):
      t = threading.Thread(target=self.get_max_fuel_cell_of_size, args=(grid, size+1,))
      self.threads.append(t)
      t.start()

    for thread in self.threads:
      thread.join()

    return str(self.winning_grid_x) + "," + str(self.winning_grid_y) + "," + str(self.max_grid_fuel_cell_value)

def main():
  print(str(Day11Puzzle2().solution(3214)))

if __name__ == "__main__":
  main()
