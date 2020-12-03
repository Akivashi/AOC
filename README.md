# AOC :snake:
Advent Of Code Solutions made using [Python 3](https://www.python.org/downloads/release)

Disclaimer: These solutions might not be the best ones out there (let alone the prettiest Python code you'll come across), but atleast i had fun creating them.

## How to run:

```
cd days/day<#day>
python Day<#day>Puzzle<#Puzzle> -i <inputvalue>
```
`<inputvalue>` being dependent on the input for that specific day.

## How to run tests:
```
cd days/day<#day>
python -m unittest tests.test_Day<#day>Puzzle<#Puzzle>
```
or by running all tests using
```
cd days/day<#day>
python -m unittest discover
```
## Setup from scratch:
```
python create_initial_files.py -location <foldername>
```
Note: creating these initial files will only create them if they do not already exist
