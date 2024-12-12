f = open("day3.txt","r")
key = "mul(x,x)"
do = "do()"
dont = "don't()"
output = 0
enabled = True
for i in range(6):
  line = f.readline()
  ldo = False
  ldont = False
  lmult=False
  count=0
  fnum=""
  lnum=""
  tlist = []
  templist = ""
  for char in line:
    if count==0:
      if char==key[0]:
        lmult=True
        ldo=False
        ldont=False
      elif char==do[0]:
        ldo=True
        ldont=False

    if ldo:
      if char==do[count]:
        count += 1
        templist += char
        if count==(len(do)):
          print("enabled")
          tlist.append(templist)
          enabled=True
          ldo=False
          ldont=False
          count = 0
          fnum = ""
          lnum = ""
          templist = ""
      elif char=="n" and count == 2:
        ldo=False
        ldont=True
        count += 1
        templist += char
      else:
        count = 0
        ldo=False
        ldont=False
        lmult=False
        fnum = ""
        lnum = ""
        templist = ""

    elif ldont:
      if char==dont[count]:
        count += 1
        templist += char
        if count==(len(dont)):
          print("disabled")
          tlist.append(templist)
          enabled=False
          ldont=False
          ldo=False
          count = 0
          fnum = ""
          lnum = ""
          templist = ""
      else:
        ldont=False
        count = 0
        fnum = ""
        lnum = ""
        templist = ""

    elif lmult:
      if enabled:
        if count==4:
          try:
            p = int(char)
            fnum+=char
            templist+=char
          except:
            if char == ",":
              templist += char
              count=6
            else:
              count=0
              fnum = ""
              lnum = ""
              templist=""
              lmult=False

        elif count == 6:
          try:
            p = int(char)
            lnum += char
            templist += char
          except:
            if char == ")":
              templist += char
              output += int(fnum) * int(lnum)
              tlist.append(templist)
              count = 0
              fnum = ""
              lnum = ""
              templist = ""
              lmult=False
            else:
              count = 0
              fnum = ""
              lnum = ""
              templist=""
              lmult=False

        elif char == key[count]:
          count+=1
          templist+=char
        else:
          count = 0
          fnum = ""
          lnum = ""
          templist = ""
          lmult=False
      else:
        count = 0
        fnum = ""
        lnum = ""
        templist = ""
        lmult=False
    else:
      count=0
      lmult=False
      ldont=False
      ldo=False
print(tlist)
print(output)
