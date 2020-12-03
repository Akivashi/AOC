from datetime import datetime

class GuardRow(object):
  def __init__(self, line):
    # self.date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
    self.date =line[1:17]
    self.event = line[19:]