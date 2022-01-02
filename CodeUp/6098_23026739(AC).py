maze = [[0 for j in range(10)] for i in range(10)]
x = 0
y = 0

for i in range(10):
  inputs = input().split()  
  
  for j in range(10):
    maze[i][j] = int(inputs[j])
    if int(maze[i][j]) == 2:
      x = i + 1
      y = j + 1

# print() 
# print(x,y) 
# 0,0 기준으로 2를 정해줌.
# 일단 무조건 오른쪽으로 가고싶어하고, 그다음 아래로.
# 2,2라는데, 배열로치면 1,1에서 출발
# 오른쪽으로가는데 벽 (1)을 만나면 아래로
# 종료조건은 오른쪽이나 아래에 벽, 혹은 2를 만날때까지

current_x = 1
current_y = 1

# print(x,y)

while True:
  maze[current_x][current_y] = 9
  if ((current_x == 8) and (current_y == 8)) or \
  (maze[current_x][current_y] == 1) :
    break
  elif (current_x == x) and (current_y == y):
    maze[current_x][current_y] = 9
    break    
  else:
    maze[current_x][current_y] = 9
    if maze[current_x][current_y+1] == 0:
      # print("move_x")
      current_y += 1
    elif maze[current_x+1][current_y] == 0:
      # print("move_y")
      current_x += 1
    elif maze[current_x+1][current_y] == 2:
      maze[current_x+1][current_y] = 9
      break
    elif maze[current_x][current_y+1] == 2:
      maze[current_x][current_y+1] = 9
      break
    else:
      break

  
# print(current_x, current_y)
# print() 

for i in range(10):
  for j in range(10):
    print(maze[i][j], end = " ")
  print() 

# print(maze)
