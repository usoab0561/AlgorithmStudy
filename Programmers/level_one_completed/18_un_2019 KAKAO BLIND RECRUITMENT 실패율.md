https://programmers.co.kr/learn/courses/30/lessons/42889

![image](https://user-images.githubusercontent.com/84604563/152914677-e2e21b9d-227c-4edb-a343-35f81a6566a1.png)

![image](https://user-images.githubusercontent.com/84604563/152914719-5fe199fc-a528-4ca8-8882-458a725f8590.png)

<img width="423" alt="image" src="https://user-images.githubusercontent.com/84604563/153097738-91d831bb-bc33-42f2-bb88-d3a4acfce66d.png">

여기에서 ```sorted(result, key=lambda x: result[x],reverse=True)```가 있을때, result는 iterable data, lambda는 inputdata : 실제함수내용 (원래는뒤에인풋값인데 sorted에서는 iterable하면서 자동으로 넣어줌) 이렇게 됨  

https://wikidocs.net/64

```python
# 11 : 12 ~ ..
# 문제는 미리 풀었는데 dictionary사용법을 잘 모름. lambda 등과 함께
# 실패율을 구해라
# 스테이지 도달 + 클리어 못함 / 스테이지 도달
# 전체 스테이지 개수 N
# 현재 스테이지 stages (1이상, 6이하) -> 1빼줘서 index랑 맞춰주자
# 실패율 높은 스테이지부터 내림차순 스테이지번호 list를 return [실패율100프로, 실패율 90프로..]

## N + 1스테이지는 도달 + 클리어임
## 실패율같으면 작은번호스테이지가 앞으로
## 도달한 유저없으면 실패율은 0

# sol
# 1. 작은 순서대로 정렬을해서 생각해보자. 어차피 stages는 순서상관없으니까
# 2. 1stage ~ 8 stage (len(stage))까지 돌면서 ratio구하자

# 내가 놓친것 1. 도달한유저없으면 실패율 0 인것 확인안해줌
# 2. lambda 모르겠음 어떻게 dict사용하는지 ㅠ 다시공부ㅋ
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
```

# 배울점
## lambda, dictionary사용법

# 배운점
## dictionary 사용법 dic = {} 해두고 dic[key] = value 로 넣는다. 초기화는 dic ={key : value}
## sorted(iterabledata, key= ..., reverse=True)
## (labmda parameter : outputs)(inputs)
## ex) sorted(dic, key=lambda x: dic[x], reverse=True) 여기에서는 inputs가 안들어감 왜냐하면 sorted에서 x가 iterable하게 자동으로 들어가서
