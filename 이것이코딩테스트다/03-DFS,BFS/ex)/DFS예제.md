##  dfs는 보통 코테에서 낮은 vertex부터 search하게 만듬. recursion하게 구현 ㄱ (depth-first search)  

<br>

```python
def dfs(graph, vertex, visited):
  visited[vertex] = True      # vertex 먼저 방문했다 해주고
  print(vertex, end= ' ')
  
  #recursion
  for i in graph[vertex]:     # 그래프 전체 돌아다니면서
    if not visited[i]:        # 안돌았으면
      dfs(graph, i, visited)  # recursion 해줌
      
graph =[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9 # [False, False, ... , False]

dfs(graph, 1, visited)
```
