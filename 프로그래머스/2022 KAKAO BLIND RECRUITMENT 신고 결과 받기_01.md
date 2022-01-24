```python
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    #print(reports)
    
    for r in set(report):
      #print(r.split()[1])
      reports[r.split()[1]] += 1

    #print(reports)

    for r in set(report):
      if reports[r.split()[1]] >= k:
        
        #print(id_list.index(r.split()[0]))

        answer[id_list.index(r.split()[0])] += 1

    return answer

#위치 반환(index)
#index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.

#>>> a = [1,2,3]
#>>> a.index(3)
#2
#>>> a.index(1)
#0
```
