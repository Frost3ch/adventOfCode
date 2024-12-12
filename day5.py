import copy
import random
f = open("day5.txt","r")
rulesa = []
rulesb = []
output = 0

for i in range(1176):
  line = f.readline().strip()
  place = line.split("|")
  rulesa.append(place[0])
  rulesb.append(place[1])
f.readline()
for j in range(1368-1176):
  line = f.readline().strip()
  data=line.split(",")
  print(data)
  print(j)
  valid=False
  swapCount = 0
  anySwap = False
  while swapCount< 800 and valid==False:
    swapped=False
    blacklist = []
    blTrigger = []
    for num in data:
      if num in blacklist:
        sindex = blacklist.index(num)
        mindex = data.index(num)
        temp = data[mindex]
        data[mindex] = data[blTrigger[sindex]]

        data[blTrigger[sindex]] = temp

        swapCount+=1
        swapped=True
        anySwap=True
      if num in rulesb:
        delLista = copy.copy(rulesa)
        delListb = copy.copy(rulesb)
        while True:
          try:
            index = delListb.index(num)
            aEqu = delLista[index]
            delLista.pop(index)
            delListb.pop(index)
            if aEqu in data[:data.index(num)]:
              valid=False
            else:
              blacklist.append(aEqu)
              blTrigger.append(data.index(num))
          except:
            break
    if swapped==False:
      valid=True
  if valid and anySwap:
    middle = int(data[int((len(data)-1)/2)])
    output += middle
print(output)




