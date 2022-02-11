https://programmers.co.kr/learn/courses/30/lessons/12922

```python
# 09:52 ~ 09:55

def solution(n):
#     lists = ['수','박']
    
#     answer = ''
#     for i in range(n):
#         if i > 1:
#             i = i % 2    
#         answer += lists[i]
#     return answer

    s = "수박" * n
    return s[:n]

```

# 배운점
## str을 곱하면 그 개수만금 만듬. 그리고 몇개냐에 따라서 자른거임
