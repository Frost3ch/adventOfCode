f=open("day1.txt","r")
l1 = []
l2 = []
similarity = 0
for i in range(1000):
    l = f.readline().strip()
    l1.append(int(l[0:5]))
    l2.append(int(l[8:]))

for i in range(1000):
    similarity += l1[i] * l2.count(l1[i])
print(similarity)

