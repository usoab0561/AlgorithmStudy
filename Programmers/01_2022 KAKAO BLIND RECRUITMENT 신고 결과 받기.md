https://programmers.co.kr/learn/courses/30/lessons/92334#

![image](https://user-images.githubusercontent.com/84604563/151920785-f0c59533-9a7d-4108-a6b3-533a89f6dcfe.png)

```python
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    #print(reports)
    #{'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}

    for r in set(report):
      # print(r.split()[1], end=' ')
      # 뒤에것만 추출
      # muzi neo frodo neo frodo
      reports[r.split()[1]] += 1
      # 뒤에것만 추출 한 뒤, dictionary에 key부분에 넣어주고 value는 1 더해줌
      
    # print(reports)
    # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    
    for r in set(report):
      if reports[r.split()[1]] >= k:
        
        # print(id_list.index(r.split()[0]))
        # 2 1 0 0
        
        answer[id_list.index(r.split()[0])] += 1
        # print(answer)
        # [0, 0, 1, 0]
        # [1, 0, 1, 0]
        # [1, 1, 1, 0]
        # [2, 1, 1, 0]
    
    return answer

#위치 반환(index)
#index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.

#>>> a = [1,2,3]
#>>> a.index(3)
#2
#>>> a.index(1)
#0

solution(	["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
```

2번째 

```python
# 신고 2번이상 당하면 게시판 이용정지
# a가 (신고한 사람 == 정지된 사람) 이면 메일을 1개 받음
# a가 (신고한사람 4명, 정지된사람 3명)이면 메일을 3개 받음

# id_list는 id_list
# report는 신고한사람 신고당한사람

def solution(id_list, report, k):
    
    # id_list_reported = {} 는 report 당한 횟수
    id_list_reported = {id : 0 for id in id_list}
    id_list_mail = [0] * len(id_list)
    # ## 'muzi' : 0 만듬
    # for id in id_list:
    #     id_list_reported[id] = 0
        
    ## 'muzi' : 1, 'frodo' : 2 만듬
    for reported in set(report):
        id_list_reported[reported.split()[1]] += 1
    
    #     #for문 2번해서 시간초과당함, but dictionary 기초사용법 특히 for문 key를 사용해서 dictionary 돌아가는거 배움
    #     # id_list_reported를 돌면서 value값이 k 이상이면 report돌면서 신고받은놈을 확인하고, id_list_mail에 추가해줌.
    # id_list_reported = {} #는 mail 받을 횟수
    #     for key in id_list_reported:
    #         if id_list_reported[key] >= k:
    #             for reported in set(report):
    #                 if reported.split()[1] == key:
    #                     id_list_mail[reported.split()[0]] += 1
    
    # print(id_list_mail)
    
    for reported in set(report): # report를 돌아야한다는점을 잘 생각해야함. 안그러면 nested loop 됨
        if id_list_reported[reported.split()[1]] >= k:
            id_list_mail[id_list.index(reported.split()[0])] += 1
            # 결국 id_list의 index에 접근해서 더해주면 됨
    return id_list_mail
    ```
