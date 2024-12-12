matrix = []
f=open("day10.txt","r")
for i in range(45):
  line = f.readline().strip()
  line = list(line)
  line = [int(x) for x in line]
  matrix.append(line)

tsum = 0
global found9s
def findTrails(loc,matrix,prevVal):
  try:
    if loc[0]>-1 and loc[0]<len(matrix) and loc[1]>-1 and loc[1]<len(matrix[0]):
      if matrix[loc[0]][loc[1]] == prevVal+1:
        if matrix[loc[0]][loc[1]] == 9:
          # if loc in found9s:
          #   return 0
          # else:
            found9s.append(loc)
            return 1
        else:
          return findTrails([loc[0]+1,loc[1]],matrix,matrix[loc[0]][loc[1]]) + findTrails([loc[0]-1,loc[1]],matrix,matrix[loc[0]][loc[1]]) + findTrails([loc[0],loc[1]-1],matrix,matrix[loc[0]][loc[1]]) + findTrails([loc[0],loc[1]+1],matrix,matrix[loc[0]][loc[1]])
      else:
        return 0
    else:
      return 0
  except:
    return 0

for y  in range(len(matrix)):
  for x in range(len(matrix[0])):
    if matrix[y][x] == 0:
      global found9s
      loc = [y,x]
      found9s = []
      tsum += (findTrails([loc[0]+1,loc[1]],matrix,matrix[loc[0]][loc[1]]) + findTrails([loc[0]-1,loc[1]],matrix,matrix[loc[0]][loc[1]]) + findTrails([loc[0],loc[1]-1],matrix,matrix[loc[0]][loc[1]]) + findTrails([loc[0],loc[1]+1],matrix,matrix[loc[0]][loc[1]]))
      print(tsum)

print(tsum)
