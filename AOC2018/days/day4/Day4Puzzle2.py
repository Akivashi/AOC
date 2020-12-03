import argparse
import re
import time
import numpy as np
import operator
from GuardRow import GuardRow
from datetime import datetime

class Day4Puzzle2(object):
  def __init__(self):
    self.day = 4
    self.puzzle = 2
    self.guards_accumulated_minutes_sleep_dict = {}

  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    events = []
    for line in lines:
      events.append(GuardRow(line))
    events.sort(key=lambda x: x.date)

    for e in events:
      if '#' in e.event:
        guard_id = self.guardduty_start(e.event)
      elif 'wakes' in e.event:
        self.guardduty_event(guard_id, e.date, False)
      elif 'falls' in e.event:
        self.guardduty_event(guard_id, e.date, True)

    longest_accumulated_sleep_minute = [0, 0, 0]
    for guard_id in self.guards_accumulated_minutes_sleep_dict.keys():
      index, value = max(enumerate(self.guards_accumulated_minutes_sleep_dict[guard_id]), key=operator.itemgetter(1))
      if int(value) > longest_accumulated_sleep_minute[2]:
        longest_accumulated_sleep_minute = [guard_id, index, value]

    return int(longest_accumulated_sleep_minute[0]) * int(longest_accumulated_sleep_minute[1])

  def guardduty_start(self, event):
    guard_id = re.findall(r'[\d.]+', event)[0]
    if guard_id not in self.guards_accumulated_minutes_sleep_dict.keys():
      self.guards_accumulated_minutes_sleep_dict.update( {guard_id : np.zeros(60, dtype=int)})
    return guard_id

  def guardduty_event(self, guard_id, event_date, falls_asleep):
    event_minute = datetime.strptime(event_date, '%Y-%m-%d %H:%M').minute
    guardSleepArray = self.guards_accumulated_minutes_sleep_dict.get(guard_id)
    for i in range(event_minute, 60):
      if(falls_asleep):
        guardSleepArray[i] += 1
      else:
        guardSleepArray[i] -= 1
    self.guards_accumulated_minutes_sleep_dict.update( {guard_id : guardSleepArray} )

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day4Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
