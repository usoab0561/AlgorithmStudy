<img width="511" alt="image" src="https://user-images.githubusercontent.com/84604563/154180663-99f11947-4ef4-4131-8d36-43b2c78d92b2.png">

https://programmers.co.kr/learn/courses/30/lessons/77485
# 주어진 값으로 돌리고, 그 돌려진 상태로 최솟값을 return해주는 문제.

```python
# 09:41 ~ 10:46
from collections import deque
def solution(rows, columns, queries):
    arr = [[0 for i in range(columns)] for j in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = (i) * (columns) + j + 1
            
    
    result = []
    
    for q in range(len(queries)):
        # lists로 index뽑기
        lists = queries[q]
        for i in range(len(lists)):
            lists[i] -= 1
        # print(lists)

        queue = deque()
        queue_max = set([])
        
        # 4,0 에서 4,2까지
        i = lists[0]
        j = lists[1]
        queue.append(arr[i][j])
        queue_max.add(arr[i][j])
        while j < lists[3]:
            queue.append(arr[i][j+1])
            queue_max.add(arr[i][j+1])
            arr[i][j+1] = queue.popleft()
            j += 1
        # print(queue)

        # 1,3 에서 4,3까지
        i = lists[0]
        j = lists[3]
        while i < lists[2]:
            queue.append(arr[i+1][j])
            queue_max.add(arr[i+1][j])
            arr[i+1][j] = queue.popleft()
            i += 1
        # print(queue)

        # 5,2 에서 5,0까지
        i = lists[2]
        j = lists[3]
        while j > lists[1]:
            queue.append(arr[i][j-1])
            queue_max.add(arr[i][j-1])
            arr[i][j-1] = queue.popleft()
            j -= 1
        # print(queue)

        # 5,0 에서 4,0까지
        i = lists[2]
        j = lists[1]
        while i > lists[0]:
            queue.append(arr[i-1][j])
            queue_max.add(arr[i-1][j])
            arr[i-1][j] = queue.popleft()
            i -= 1
        # print(queue)
        
        # for i in range(rows):
        #     for j in range(columns):
        #         print(arr[i][j], end= ' ')
        #     print()
        result.append(min(queue_max))
    
    
    return result
```    

# 배운점
## lists로 쿼리 뽑을 필요 없다. [[2,3,4,5], [5,6,7,8], [9,10,11,12]] 이런 쿼리가 있을때

```python 
for a,b,c,d in queries:
    stack = []
    r1, c1, r2, c2 = a-1, b-1, c-1, d-1
```  
이런식으로 뽑아도 됨. 3번반복돼서 a,b,c,d가 뽑힌다. 이처럼 r1, c1, r2, c2로 지정해서 해주면 좀 더 빠르게 풀 수 있지 않았을까
