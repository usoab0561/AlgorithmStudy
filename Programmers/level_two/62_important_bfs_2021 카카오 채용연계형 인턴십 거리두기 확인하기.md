https://programmers.co.kr/learn/courses/30/lessons/81302#fn1  

<br>

https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python 

<br>

```python
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5):                          # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:                             # 시작점 P 마다 전체적으로 연결된거 찾을거다. 
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]     # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]    # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            
            x, y = queue.popleft()              # 시작점으로부터 움직인 좌표
            print()
            print(x,y)
            print()
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 하상

            for i in range(4):                  # 시작점으로부터 움직인 좌표 기준 좌우상하 움직임.

                nx = x + dx[i]
                ny = y + dy[i]
                print(nx,ny)        

                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    
                    if p[nx][ny] == 'O':                            # 연결되어있으면 큐에 갱신, 방문했다고 말해주기
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    
                    if p[nx][ny] == 'P' and distance[x][y] <= 1:    # 길이 1이하인경우만 return 0
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        print(i)
        answer.append(bfs(i))
        print()
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

```
