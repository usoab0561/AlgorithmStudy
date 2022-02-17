<img width="534" alt="image" src="https://user-images.githubusercontent.com/84604563/153986836-6f73c160-532c-4568-8055-23c56731d877.png">

<img width="1024" alt="image" src="https://user-images.githubusercontent.com/84604563/153983514-82316bc0-5a1c-43e3-a3f0-83b6174a6d3a.png">

<img width="997" alt="image" src="https://user-images.githubusercontent.com/84604563/153983475-842d3abc-51be-4517-9dd7-adc6e9e86465.png">  

https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3  

```python
#BFS 풀이
from collections import deque
def solution(numbers, target):
    answer = 0
    leaves = deque([0])
    for num in numbers:
        length = len(leaves)
        for _ in range(length):
            leaves.append(leaves[0] + num)
            leaves.append(leaves[0] - num)
            leaves.popleft()
    
    return leaves.count(target)
```

```python
#BFS 풀이
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer
```    

## 같은 깊이당 지금 현재의 leaves를 계속 생각해주면서 갱신해주면 된다. (부모 leaves를 뺴서 지금 level의 값을 수정하는 방식)



<img width="939" alt="image" src="https://user-images.githubusercontent.com/84604563/153986741-302aa324-88cd-4dda-929b-9fcc917428a5.png">

```python
#DFS풀이
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    if(idx== len(numbers) and target == value):
        answer += 1
        print(idx, value, True)
        
        return
    if(idx == len(numbers)):
        print(idx, value)
        return

    print(idx, value)   
    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
    
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
```    
## 깊이의 끝까지 가게하고, 깊이의 끝을 만났을때 & 타겟숫자랑 같을때 answer을 더해줌. 재귀써서 (좌,우로)깊이끝까지가게하고 L,V,R 순으로 돌게함

# 결국 문제는 모든 수를 다 사용해서, target이 맞는 수를 찾는것이었다. 그래서 모든 요소의 경우의 수를 마지막 index까지 다 생각한다 -> bfs/dfs 마지막 깊이일때 확인한다로 생각해야함
