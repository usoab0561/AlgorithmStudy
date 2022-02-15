https://www.acmicpc.net/problem/2606

<img width="1165" alt="image" src="https://user-images.githubusercontent.com/84604563/153990233-60c1770c-63cd-455d-9442-2b01eb165541.png">
<img width="1176" alt="image" src="https://user-images.githubusercontent.com/84604563/153990253-4093e996-c5b0-4f2c-a377-0c8255c27aa3.png">

1. 2차원배열로 노드들을 연결해줌.
2. discovered라는 리스트 만들어서 방문했는지 채크해줌. 만약에 방문안했으면 discovered에 넣어주고, 큐에 방문안한 노드 넣어줌.
3. 결국 discovered는 시작값을주어주면, bfs순으로 연결된 모든 노드들을 순회함.

```python
from collections import deque

computer_num = int(input())
pair = int(input())

graph = [[0] * (computer_num + 1) for _ in range(computer_num + 1)]
print()
print(graph)

for _ in range(pair):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1
print()
print(graph)

# 너비 우선 탐색
def bfs(start_v):
  discoverd = [start_v]
  # deque 생성
  queue = deque()
  queue.append(start_v)
  
  while queue:
    v = queue.popleft()

    for w in range(len(graph[start_v])):
      if graph[v][w] == 1 and (w not in discoverd):
        discoverd.append(w)
        queue.append(w)

  return discoverd

print(len(bfs(1))-1)
```
