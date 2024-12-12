f=open("day9.txt","r")
line = f.readline()
dmap = list(line)
dmap = [int(x) for x in dmap]
flist = []

for i in range(len(dmap)):
  num = dmap[i]
  if num!=0:
    if i%2==0:
      flist.append([i//2] * num)
    else:
      flist.append(["."] * num)

print(flist)

end = -1
while True:
  if 0 > len(flist)+end:
    break
  while flist[end][0] == ".": end -= 1
  c=0
  while c<len(flist)+end:
    if flist[c][-1] == ".":
      if len(flist[c]) >= len(flist[end]):
        length = len(flist[c])
        flist.pop(c)
        flist.insert(c,flist[end])
        if length-len(flist[c]) >0:
          flist.insert(c+1,("."*(length-len(flist[c]))))
        flist[end] = "." * len(flist[end])
        break
    c+=1
  end-=1

print(flist)

sum = 0

flatList = [j for sub in flist for j in sub]
print(flatList)
for x in range(len(flatList)):
  if flatList[x]!=".":
    num = int(flatList[x])
    sum += num * x

print(sum)
