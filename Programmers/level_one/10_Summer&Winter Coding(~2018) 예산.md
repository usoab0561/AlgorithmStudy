![image](https://user-images.githubusercontent.com/84604563/152505987-3d362c42-a500-4ea0-a7c1-7d8b47f3d926.png)
https://programmers.co.kr/learn/courses/30/lessons/12982

solved
```python
def solution(d, budget):
    total = 0
    count = 0
    
    d.sort()
    
    for i in d:
        if total + i > budget:
            break
        elif total < budget:
            total += i
            count += 1
    
    answer = 0
    return count
```

- 남 풀이 : budget에서 빼줌  
```python
def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer
```


# 배운점

## 역시 이런문제는 result를 먼저 생각해야해. 괜히 순서나 from itertools import combinations로 찾아내려고하지말고 result만 생각하면 쉬운문제
