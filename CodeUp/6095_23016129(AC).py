n = int(input())

nestedList = [[0 for j in range(19)] for i in range(19)]

for i in range(n):
  inputs = input().split()  
  nestedList[int(inputs[0])-1][int(inputs[1])-1] = 1

for i in range(19):
  for j in range(19):
    if nestedList[i][j] == 0:
      print(0, end = ' ')
    else:
      print(1, end = ' ')

  print(" ")    
