solved in 15min

더해서 소수구하는문제
https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3

```python
# 3개 수 더했을때 소수가되는 경우의수
# nums에서 3개 더해서 소수가 되는 경우의수
# 1. 조합구하고
# 2. 소수 구하기
from itertools import combinations
from math import sqrt
def solution(nums):
    
    answer = 0
    nums_combi = list(combinations(nums, 3))
    # print(nums_combi)
    # print(sum(nums_combi[0]))
    for i in range(len(nums_combi)):
        total = sum(nums_combi[i])
        # print(total)
        # print(int(sqrt(total)))
        # print()
        j = 1
        check = True
        while j < int(sqrt(total)):
            j += 1
            if total % j == 0:
                check = False
                break
        
        # print(check)
        
        answer = answer + 1 if check else answer
        
    return answer
```

# 배운점
## from itertools import combinations다. import combination 아니고 from itertools먼저임
## from math import sqrt
## 42서울한게 도움이 됐네. sqrt이전까지만 판단해도됨. 이산수학인가에서 나오는 내용
## answer = answer + 1 if check else answer
## sum(tuples)하면 tuples안에있는값 다 더해줌 sum((1, 2, 3)) -> 6
