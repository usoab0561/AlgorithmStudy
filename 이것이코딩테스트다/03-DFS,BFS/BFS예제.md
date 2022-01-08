## Breath First Search는 가까운거부터. 보통 bfs가 더 빠름 deque, from collection import deque큐사용

```python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    
    for i in graph[v]:  # 해당 vertex와 연결된, 아직 방문하지 않은 vertex들을 queue에다가 append해줌. push
      if not visited[i]:
        queue.append(i)
        visited[i] = True


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

bfs(graph, 1, visited)

```

