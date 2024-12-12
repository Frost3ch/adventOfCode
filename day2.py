f=open("day2.txt","r")
sumOfSafe = 0
def checkSafe(l):
  ascend = None
  if l[0]-l[1] < 0:
    ascend = True
  elif l[0]-l[1] >0:
    ascend = False
  prev = l[0]
  for x in range(1,len(l)):
    curr = l[x]
    if curr==prev:
      a=0
      for i in range(len(l)):
        nl = l.copy()
        nl.pop(i)
        a = max(checkSafe2(nl),a)
        print(a)
      return a
    elif (prev-curr<0) != ascend:
      a = 0
      for i in range(len(l)):
        nl = l.copy()
        nl.pop(i)
        a = max(checkSafe2(nl), a)
        print(a)
      return a
    elif abs(curr-prev) >3:
      a = 0
      for i in range(len(l)):
        nl = l.copy()
        nl.pop(i)
        a = max(checkSafe2(nl), a)
        print(a)
      return a
    prev = curr
  return 1

def checkSafe2(l):
  ascend = None
  if l[0]-l[1] < 0:
    ascend = True
  elif l[0]-l[1] >0:
    ascend = False
  prev = l[0]
  for x in range(1,len(l)):
    curr = l[x]
    if curr==prev:
      return 0
    if (prev-curr<0) != ascend:
      return 0
    if abs(curr-prev) >3:
      return 0
    prev = curr
  return 1

for i in range(1000):
  line = f.readline().strip()
  l = line.split()
  l = [int(x) for x in l]
  print(l)
  sumOfSafe += checkSafe(l)
print(sumOfSafe)

