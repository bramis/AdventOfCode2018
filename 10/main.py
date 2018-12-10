import re

def main():
  file = open("input.txt", "r")
  filelines = file.readlines()

  pointDictList = []
  for line in filelines:
    match = re.search("^position=<\s?([0-9-]*), \s?([0-9-]*)> velocity=<\s?([0-9-]*), \s?([0-9-]*)>", line)
    pointDictList.append({
      'pX': match.group(1),
      'pY': match.group(2),
      'vX': match.group(3),
      'vY': match.group(4),
    })

  print pointDictList

if __name__ == "__main__":
  main()