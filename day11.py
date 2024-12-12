f = open("day11.txt","r")
line = f.readline().strip()
stones = line.split()
stones = [int(x) for x in stones]
print(stones)
mem = {}

def solve(x,t):
  if (x,t) in mem:
    return mem[(x,t)]
  if t<1:
    ret = 1
  elif x==0:
    ret = solve(1,t-1)
  elif len(str(x))%2==0:
    left = int(str(x)[:len(str(x)) // 2])
    right = int(str(x)[len(str(x)) // 2:])
    ret = solve(left,t-1) + solve(right,t-1)
  else:
    ret = solve(x*2024,t-1)
  mem[(x,t)] = ret
  return ret

outp = 0

for x in stones:
  print(x)
  outp += solve(x,75)

print(outp)
