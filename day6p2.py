import copy
f = open("day6.txt","r")
ogMap = []
Ogloc = [0,0]
loopTracker = 0

for i in range(130):
  line = list(f.readline().strip())
  if "^" in line:
    Ogloc = [i,line.index("^")]
  ogMap.append(line)

tCells = []

wMap = copy.deepcopy(ogMap)
gloc = copy.deepcopy(Ogloc)
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
  if gloc not in tCells:
    tCells.append(gloc)

for x in range(len(tCells)):
  print(str(x/len(tCells)*100) + "%")
  wMap = copy.deepcopy(ogMap)
  gloc = copy.deepcopy(Ogloc)
  if wMap[tCells[x][0]][tCells[x][1]]!="^":
    wMap[tCells[x][0]][tCells[x][1]] = "#"

  wMap[gloc[0]][gloc[1]] = "X"
  dir = [[-1,0],[0,1],[1,0],[0,-1]]
  whichDir = 0
  allGlocs=[[gloc,whichDir]]
  looping=False

  while True:
    newPos = [gloc[0]+dir[whichDir][0],gloc[1]+dir[whichDir][1]]
    if newPos[0]>len(wMap)-1 or newPos[0]<0 or newPos[1]>(len(wMap[0]))-1 or newPos[1]<0:
      break
    if wMap[newPos[0]][newPos[1]]=="#":
      whichDir = (whichDir+1)%4
      newPos = gloc
    gloc = newPos
    if [gloc,whichDir] in allGlocs:
      looping=True
      break
    allGlocs.append([gloc,whichDir])
    wMap[gloc[0]][gloc[1]] = "X"
  if looping:
    loopTracker+=1
print(loopTracker)
    # print(sum(x.count('X') for x in wMap))