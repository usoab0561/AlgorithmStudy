d = [[0 for j in range(20)] for i in range(20)]

# a = input().split()

# d[0][0] = a[0]
# d[0][1] = a[1]
# ...
# d[0][18] = a[18]

# d[1][0] = a[0]
# d[1][1] = a[1]
# ...
# d[1][18] = a[18]

for i in range(19):
  a = input().split()
  for j in range(19):
    d[i][j] = int(a[j])

n = int(input())

# change = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
  inputs = input().split()
  row = int(inputs[0]) - 1
  col = int(inputs[1]) - 1

  for j in range(19):
    d[row][j] =  0 if (d[row][j] == 1) else 1
  for k in range(19):
    d[k][col] = 0 if d[k][col] == 1 else 1
  

for i in range(19):
  for j in range(19):
    print(d[i][j], end =" ")
  print()
