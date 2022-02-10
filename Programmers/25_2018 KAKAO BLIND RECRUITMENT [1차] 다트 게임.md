solved
```python
# 12:20 ~ 12:47
# 점수계산

#3번기회 0~10
# 점수,보너스,(옵션)

def solution(dartResult):
    dartResult = list(map(str,dartResult))
    print(dartResult)
    
    i = 0
    total = []
    tmp = 0
    while i < len(dartResult):
        if dartResult[i].isnumeric():
            if i > 0 and dartResult[i-1].isnumeric():
                total[-1] = total[-1] * 10 + int(dartResult[i])
            else:
                total.append(int(dartResult[i]))
        elif dartResult[i] == 'S':
            total[-1] = total[-1] 
        elif dartResult[i] == 'D':
            total[-1] = total[-1]**2
        elif dartResult[i] == 'T':
            total[-1] = total[-1]**3
        elif dartResult[i] == '*':
            if len(total) == 1:
                total[0] = total[0] * 2
            else:
                total[-1] = total[-1] * 2
                total[-2] = total[-2] * 2
        elif dartResult[i] == '#':
            total[-1] = -total[-1]
        i = i+1
        print(total)
    
    return sum(total)

```

<img width="1179" alt="image" src="https://user-images.githubusercontent.com/84604563/153335091-ab3f066e-bafe-4a01-b2a5-56e110e3cc16.png">

이거 공부 ㄱ
https://programmers.co.kr/learn/courses/30/lessons/17682/solution_groups?language=python3

## 문제 조건들이 난해하게 많아서 시간이 좀 더 걸렸다
## 역시 이렇게 긴 str문제는 while문으로 i까지 직접 만들어주는게 정신건강에 좋음
## 문제 조건대로 우선 숫자 먼저 list만들어 넣어주고 조건들은 따로 생각하는게 좋은듯

## int숫자면 list[0] = -list[0]같이 만들어 줄 수 있음
## list는 최고인게 list[-2] 같은 연산도 잘 되네
