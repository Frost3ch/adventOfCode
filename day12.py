f = open("day12.txt","r")
matrix = []
for i in range(140):
  line = f.readline().strip()
  matrix.append(list(line))
print(matrix)

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
global searched
global area
maxSearched = []
searched = []

def calcScore(loc,matrix):
  score = 4
  for dir in dirs:
    if loc[0]+dir[0]>=0 and loc[0]+dir[0]<len(matrix) and loc[1]+dir[1]>=0 and loc[1]+dir[1]<len(matrix[0]):
      if matrix[loc[0]+dir[0]][loc[1]+dir[1]] == matrix[loc[0]][loc[1]]:
        score -=1
  return score

def findShape(loc, matrix):
  global searched
  ogcell = matrix[loc[0]][loc[1]]

  for dir in dirs:
    if loc[0]+dir[0]>=0 and loc[0]+dir[0]<len(matrix) and loc[1]+dir[1]>=0 and loc[1]+dir[1]<len(matrix[0]):
      checkCell = matrix[loc[0]+dir[0]][loc[1]+dir[1]]
      if checkCell == ogcell:
        if [loc[0] + dir[0], loc[1] + dir[1]] not in searched:
          searched.append([loc[0] + dir[0], loc[1] + dir[1]])
          findShape([loc[0] + dir[0], loc[1] + dir[1]],matrix)

total = 0

for y in range(len(matrix)):
  for x in range(len(matrix[0])):
    cell = matrix[y][x]
    if [y,x] not in maxSearched:
      searched = [[y,x]]
      findShape([y,x],matrix)
      maxSearched += searched
      perimeter = 0
      for item in searched:
        perimeter += calcScore(item,matrix)
      print(perimeter)
      print(len(searched))
      total += len(searched) * perimeter

print(total)




