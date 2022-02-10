solved
https://programmers.co.kr/learn/courses/30/lessons/17681

<img width="403" alt="image" src="https://user-images.githubusercontent.com/84604563/153329818-28054818-d797-4ffc-98b8-fc7f45ae0195.png">

<img width="444" alt="image" src="https://user-images.githubusercontent.com/84604563/153329888-916735dc-5990-4b46-a1cd-be60f7640154.png">

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

```python
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
 ```
 
# 배운점
## list comprehension 아직 안 익숙. lists = [ [0 for i in range(n)] for j in range(n)]
## 간단한거 구현하고 (2진수만드는거) 전체를 만들때, 예시로 든 숫자(나는 5를 2진수로만들려고했음) 이거를 전체범위 input으로 바꿔야하는데 안바꿔서 헤맴
## 그러니까 조금 더 주의해서 예시를 전체로 바꿀때 생각해줘야함.
## bin 사용하면 2진수로 그냥 바꿔줌. 그런데 0b00001 뭐 이런식으로나와서 a12 = str(bin(i|j)[2:]) 이렇게 자른거임.
## '2'.rjust(5, '0') -> 00002 로 해줌. 자매품으로 str.ljust('int', 'chr') 
