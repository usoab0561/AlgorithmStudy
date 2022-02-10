solved
https://programmers.co.kr/learn/courses/30/lessons/17681

```python
# 11:17 ~ 11:51
def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    
    #convert 9 가 들어왔을때 1001이 나오게
    # inputs = 5
    arr_one = []
    arr_two = []
    for i in range(len(arr1)):
        inputs = arr1[i]
        lists = []
        while inputs > 0:
            tmp = inputs % 2
            tmp = '#' if tmp == 1 else ' '
            lists.append(tmp)
            inputs = inputs // 2

        while len(lists) != n:
            lists.append(' ')
        lists.reverse()
        arr_one.append(lists)
    
    for i in range(len(arr2)):
        inputs = arr2[i]
        lists = []
        while inputs > 0:
            tmp = inputs % 2
            tmp = '#' if tmp == 1 else ' '
            lists.append(tmp)
            inputs = inputs // 2

        while len(lists) != n:
            lists.append(' ')
        lists.reverse()
        arr_two.append(lists)
    # print(arr_one)
    # print(arr_two)
    
    
    for i in range(n):
        for j in range(n):
            if arr_one[i][j] == '#' or arr_two[i][j] == '#':
                answer[i] += '#'
            else:
                answer[i] += ' '
                # print(answer[i][j])
        # answer[i] = answer[i]
    return answer
```

# 배운점
## list comprehension 아직 안 익숙. lists = [ [0 for i in range(n)] for j in range(n)]
## 간단한거 구현하고 (2진수만드는거) 전체를 만들때, 예시로 든 숫자(나는 5를 2진수로만들려고했음) 이거를 전체범위 input으로 바꿔야하는데 안바꿔서 헤맴
## 그러니까 조금 더 주의해서 예시를 전체로 바꿀때 생각해줘야함.
