f = open("day6.txt","r")
wMap = []
gloc = [0,0]
for i in range(130):
  line = list(f.readline().strip())
  if "^" in line:
    gloc = [i,line.index("^")]
  wMap.append(line)

wMap[gloc[0]][gloc[1]] = "X"

dir = [[-1,0],[0,1],[1,0],[0,-1]]
whichDir = 0
while True:
  newPos = [gloc[0]+dir[whichDir][0],gloc[1]+dir[whichDir][1]]
  if newPos[0]>len(wMap)-1 or newPos[0]<0 or newPos[1]>(len(wMap[0]))-1 or newPos[1]<0:
    break
  if wMap[newPos[0]][newPos[1]]=="#":
    whichDir = (whichDir+1)%4
    newPos = gloc
  gloc = newPos
  wMap[gloc[0]][gloc[1]] = "X"
for row in wMap:
  print(row)
print(sum(x.count('X') for x in wMap))

