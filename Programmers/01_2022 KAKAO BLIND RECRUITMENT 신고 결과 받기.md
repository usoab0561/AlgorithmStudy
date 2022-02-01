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
