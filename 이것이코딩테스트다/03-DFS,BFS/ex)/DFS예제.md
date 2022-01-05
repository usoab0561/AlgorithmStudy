##  dfs는 보통 코테에서 낮은 vertex부터 search하게 만듬. recursion하게 구현 ㄱ (depth-first search)  

<br>

```python
n,m = map(int, input().split())

graph = []
for i in range(n):                                                  # 1 1 1 1 1 1 ... 이런거 입력받는거
  graph.append(list(map(int, input())))


def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  else:
    return False
  
result = 0

for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1
 

print(result)
```
![image](https://user-images.githubusercontent.com/84604563/148207607-691cb908-787b-49ce-8017-9716647bb0cc.png)
