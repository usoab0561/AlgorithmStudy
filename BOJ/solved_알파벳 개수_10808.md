```python
import sys
N = list(map(str, sys.stdin.readline().rstrip()))
answer = [0 for _ in range(26)]

for i in N:
  tmp = ord(i) - 97
  answer[tmp] += 1
  
print(*answer)
```
