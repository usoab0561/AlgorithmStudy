h,w = input().split()
n = input() # stick개수

h = int(h)  
w = int(w)
n = int(n)

base = [[0 for i in range(w)] for j in range(h)]
# print(base)
# stick = [[0 for i in range(4)] for j in range(n)]
# print(stick)

for i in range(n):
  l,d,x,y = input().split() 
  l = int(l)  
  d = int(d)
  x = int(x)-1
  y = int(y)-1

  for j in range(l):
    if (d == 0):
      base[x][y+j] = 1
    else:
      base[x+j][y] = 1
  
  # print(base)
# print(base)
for i in range(h):
  for j in range(w):
    print(base[i][j], end =" ")
  print()

  # stick[i][0] = int(l) 
  # stick[i][1] = int(d)
  # stick[i][2] = int(x) - 1
  # stick[i][3] = int(y) - 1 
  

