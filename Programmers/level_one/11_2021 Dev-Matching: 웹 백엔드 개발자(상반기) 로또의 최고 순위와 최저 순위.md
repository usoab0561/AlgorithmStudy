![image](https://user-images.githubusercontent.com/84604563/152510365-4fa2d1a4-96e5-4ff0-b2a6-d1bc5b621137.png)
https://programmers.co.kr/learn/courses/30/lessons/77484#fn1

solved
```python
def solution(lottos, win_nums):
    
    total = 0
    for i in win_nums:
        if lottos.count(i) > 0:
            total += 1
    
    zero_count = lottos.count(0)
    
    grade = [6,6,5,4,3,2,1]
    
    if zero_count == 0:
        print(total)
        return [grade[total], grade[total]]
    
    
    # print(grade[total + zero_count])
    
    #print(grade[total])
    return [grade[total + zero_count], grade[total]]
    
    # 여기에서 grade[total - zero_count] 라고 zero_count를 뺴야하나 생각했음.
    # 근데 문제 제대로 생각해보면 0이 나올떄 주는게아니라 현상유지임. 이렇게 문제이해를 제대로해야함.
    # answer = []
    # return answer
```

# 배운점

## grade[total - zero_count] 라고 zero_count를 뺴야하나 생각했음.
## 근데 문제 제대로 생각해보면 0이 나올떄 주는게아니라 현상유지임. 이렇게 문제이해를 제대로해야함.
