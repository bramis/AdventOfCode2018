import re
import numpy as np
import sys
import time

def move(points):
  for point in points:
    point['pX'] += point['vX']
    point['pY'] += point['vY']

  return points

def displayMatrice(matrice):
  sys.stdout.flush()
  for line in matrice:
    for col in line:
      sys.stdout.write('#' if col == 1 else '.')
    sys.stdout.write('\n')

def main():
  file = open("input.txt", "r")
  filelines = file.readlines()

  pointDictList = []
  for line in filelines:
    match = re.search("^position=<\s?([0-9-]*), \s?([0-9-]*)> velocity=<\s?([0-9-]*), \s?([0-9-]*)>", line)
    pointDictList.append({
      'pX': int(match.group(1)),
      'pY': int(match.group(2)),
      'vX': int(match.group(3)),
      'vY': int(match.group(4)),
    })

  for t in range(100000):
    minX = min([point['pX'] for point in pointDictList])
    maxX = max([point['pX'] for point in pointDictList])
    minY = min([point['pY'] for point in pointDictList])
    maxY = max([point['pY'] for point in pointDictList])

    print minX, maxX, minY, maxY

    dec = 100
    print 'TIME:' + str(t) + ' SECONDS'
    if minX + dec >= maxX and minY + dec >= maxY:
      for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
          if (x, y) in [(point['pX'], point['pY']) for point in pointDictList]:
            print '#',
          else:
            print '.',
        print
    move(pointDictList)

if __name__ == "__main__":
  main()