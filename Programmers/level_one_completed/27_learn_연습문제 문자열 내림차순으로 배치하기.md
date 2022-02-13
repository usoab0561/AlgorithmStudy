https://programmers.co.kr/learn/courses/30/lessons/12917/solution_groups?language=python3

```python
# 09:38~ 09:40
def solution(s):

    answer = list(map(str, s))
    answer.sort(reverse=True)
    
    return "".join(answer)
```    


```python
def solution(s):
    return ''.join(sorted(s, reverse=True))
```

## s는 str

# 배운점

## sorted는 sort된 list로 return해준다. 그리고 str도 정렬가능함!!
