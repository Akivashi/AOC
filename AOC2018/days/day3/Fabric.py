import re

class Fabric(object):
  def __init__(self, line):
    splitline = re.findall(r'[\d.]+', line)
    self.id = int(splitline[0])
    self.top = int(splitline[1])
    self.left = int(splitline[2])
    self.height = int(splitline[3])
    self.width = int(splitline[4])