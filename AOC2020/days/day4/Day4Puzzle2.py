import argparse
import re

class Day4Puzzle2(object):
  def __init__(self):
    self.day = 4
    self.puzzle = 2

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
  byr = int(passport.get('byr'))
  iyr = int(passport.get('iyr'))
  eyr = int(passport.get('eyr'))
  hgt = passport.get('hgt')
  hcl = passport.get('hcl')
  ecl = passport.get('ecl')
  pid = passport.get('pid')
  if(byr >= 1920 and byr <=2002 and
     iyr >= 2010 and iyr <=2020 and
     eyr >= 2020 and eyr <=2030 and
     validate_hgt(hgt) and
     validate_hcl(hcl) and
     validate_ecl(ecl) and
     validate_pid(pid)):
    return 1
  else:
    return 0

def validate_hgt(hgt):
  rule = re.compile("(\d*)(cm|in)")
  passed = rule.search(hgt)
  if passed:
    height = int(passed.group(1))
    unit = passed.group(2)
    if((unit == 'cm' and height >= 150 and height <= 193) or
       (unit == 'in' and height >= 59 and height <= 76)):
      return True
  return False

def validate_hcl(hcl):
  rule = re.compile("#[0-9a-f]{6}$")
  passed = rule.search(hcl)
  if passed:
    return True
  return False

def validate_ecl(ecl):
  rule = re.compile("^[a-z]{3}$")
  passed = rule.search(ecl)
  if passed:
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_ecl
  return False

def validate_pid(pid):
  rule = re.compile("^\d{9}$")
  passed = rule.search(pid)
  if passed:
    return True
  return False

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
  print(str(Day4Puzzle2().solution(args["input"])))

if __name__ == "__main__":
  main()
