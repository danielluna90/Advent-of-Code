import os
from typing import List, Dict

def Puzzle1() -> None:
  f = open(os.path.join(os.path.dirname(__file__), "inputs", "Day1.txt"))

  input: List[str] = f.readlines()

  sum: int = 0

  for line in input:
    listOfDigits: List[int] = []

    for c in line:
      if c.isdigit():
        listOfDigits.append(int(c))

    sum += listOfDigits[0] * 10 + listOfDigits[-1]

  print(f"Calibration Number Sum: {sum}")

  f.close()

def Puzzle2() -> None:
  f = open(os.path.join(os.path.dirname(__file__), "inputs", "Day1.txt"))

  input: List[str] = f.readlines()
  strDigits: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
  }

  sum: int = 0

  for line in input:
    listOfDigits: List[int] = []

    for index, c in enumerate(line):
      if c.isdigit():
        listOfDigits.append(int(c))
      else:
        len3 = line[index : index + 3]
        len4 = line[index : index + 4]
        len5 = line[index : index + 5]

        if strDigits.get(len3):
          listOfDigits.append(strDigits[len3])
          index += 3
        elif strDigits.get(len4):
          listOfDigits.append(strDigits[len4])
          index += 4
        elif strDigits.get(len5):
          listOfDigits.append(strDigits[len5])
          index += 5

    sum += listOfDigits[0] * 10 + listOfDigits[-1]

  print(f"Calibration Number 2 Sum: {sum}")

  f.close()

if __name__ == "__main__":
  Puzzle1()
  Puzzle2()