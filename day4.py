import copy

f = open("day4.txt","r")
global matrix
matrix = []
for i in range(140):
  line = list(f.readline().strip())
  matrix.append(line)


def rotate(matrix):
  n = len(matrix)
  m = len(matrix[0])
  # Transpose the matrix
  transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
  # Reverse each row
  rotated_matrix = [[row[i] for i in range(m - 1, -1, -1)] for row in transposed_matrix]
  return rotated_matrix

global foundNo
foundNo=0
def csc(oCrds,cellsToCheck,wts,matrix):
  global foundNo
  p = False
  r = copy.deepcopy(oCrds[0])
  c = copy.deepcopy(oCrds[1])
  try:
    if matrix[r][c] == "M":
      if matrix[r+cellsToCheck[0][0]][c+cellsToCheck[0][1]] == "S":
        if matrix[r+cellsToCheck[1][0]][c+cellsToCheck[1][1]] == "A":
          if matrix[r + cellsToCheck[2][0]][c + cellsToCheck[2][1]] == "M":
            if matrix[r + cellsToCheck[3][0]][c + cellsToCheck[3][1]] == "S":
              foundNo +=1
  except:
    pass
  return p
def FindWord(wts):
  global foundNo, matrix
  w = False
  for i in range(4):
    for r in range(len(matrix)):
      row = matrix[r]
      for c in range(len(row)):
        cell = row[c]
        if cell == 'M':
          oCrds = [r,c]
          cellsToCheck = [[0, 2], [1, 1], [2, 0], [2, 2]]
          e = csc(oCrds, cellsToCheck, wts ,matrix)
          if e:
            w = True
    matrix = rotate(matrix)
  print(foundNo)
  if w == False:
    print("Word not found.")

def loop():
  while True:
    wts = str(input("Enter word to find: ")).upper()
    if wts == "EXIT":
      print("EXITING...")
      break
    if len(wts)>0:
      FindWord(wts)


loop()


