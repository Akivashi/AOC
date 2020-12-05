import argparse

class Day4Puzzle1(object):
  def __init__(self):
    self.day = 4
    self.puzzle = 1

  # make sure to add newlines at the end of the input file, otherwise the result might not be correct
  def solution(self, inputfile):
    with open(inputfile,"r") as file:
      lines = file.readlines()
    passports = create_passports(lines)
    valid_count = 0
    for passport in passports:
      valid_count += validate(passport)
    return valid_count

def validate(passport):
  mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # optional: , 'cid']
  for mandatory_field in mandatory_fields:
    if mandatory_field in passport:
      continue
    else:
      return 0
  return 1

def create_passports(lines):
  passport_lines = []
  passport_line = ''
  for n in range(len(lines)):
    line = lines[n].strip()
    if line == '':
      d = dict(s.split(':') for s in passport_line.split(' '))
      passport_lines.append(d)
      passport_line = ''
    else:
      if passport_line == '':
        passport_line += line
      else:
        passport_line = passport_line + ' ' + line
  return passport_lines

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="input value", type=str)
  args = vars(ap.parse_args())
  print(str(Day4Puzzle1().solution(args["input"])))

if __name__ == "__main__":
  main()
