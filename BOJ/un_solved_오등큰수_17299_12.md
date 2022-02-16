<img width="1186" alt="image" src="https://user-images.githubusercontent.com/84604563/154186932-3a8043c4-d49e-4890-9b49-0c4a599c028c.png">
https://www.acmicpc.net/problem/17299  

counter, i는 한번만돌고, stack에 index를 넣어서 앞에 값들 다 바꿔주는 문제!  
왜 stack을 쓰냐면은 오른쪽에 있는 요소값에따라 이미 나온 요소의 값을 비교하고 바꾸기 떄문!  

```python
import sys
from collections import Counter
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

NGF = [-1 for _ in range(len(A))]
# make NGF

stack = []
counters = dict(Counter(A))
# make counters as dictionary
# print(counters)

for i in range(len(A)):
  if not stack:  
  # when stack is empty, append index
    stack.append(i)
  else:
    if counters[A[i]] > counters[A[stack[-1]]]:
    # when 요소에 나온 개수보다 더 많으면 바꿔줄거임    
      while stack and counters[A[i]] > counters[A[stack[-1]]]:
        # 스텍이 비어있지않고, 요소에 나온 개수보다 많을때까지 계속 pop해주면서 바꿔줌
        NGF[stack.pop()] = A[i]
    stack.append(i)
    # 비교 다 하고도 마지막에 index 넣어줘서 다음에 비교할 수 있게 해줌 
  # print(i)
  # print(NGF)
  # print(stack)
  
print(*NGF)
```
