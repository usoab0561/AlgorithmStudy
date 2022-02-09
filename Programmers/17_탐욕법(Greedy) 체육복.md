https://programmers.co.kr/learn/courses/30/lessons/42862#
solved  

```python
# 10 : 31 ~ 11 : 03
# 다풀고 오래걸린이유
# 1. student 자꾸 studnet 라고씀 => stu로 쓰자
# 2. if문에서 조건걸고 == 를 썼는데 대입할떄도 자꾸 ==로씀. 주의!!!

#  3 (4) 5 . 4번은 3,5번만 빌려 줄 수 있다
# 최대한 많은 학생이 빌려야함
# 여분있는애도 lost당하면 없음

# 1. 전체수로 list 만들어줌.
# 2. lost한걸로 일단 체육복개수 정해줌
# 3. reverse한걸로 체육복개수 정해줌

def solution(n, lost, reserve):
    
    student = [1 for i in range(n)]
    # print(student)
    for i in lost:
        student[i-1] -= 1
    # print(student)
    for i in reserve:
        student[i-1] += 1
    # print(student)
    
    if student[0] == 2 and student[1] == 0:
        student[0] = 1
        student[1] = 1
        
    for i in range(1, len(student)-1):
        if student[i] == 2:
            if student[i-1] == 0:
                student[i] -= 1
                student[i-1] += 1
            elif student[i+1] == 0:
                student[i] -= 1
                student[i+1] += 1
    # print(student)
    # print(len(student)-1)
    if student[len(student)-1] == 2 and student[len(student)-2] == 0:
        student[len(student)-1] = 1
        student[len(student)-2] = 1
            
    # print(student)
    
    answer = len(student) - student.count(0)
    return answer
 ```
 
 # 배운점
## 다 풀고 오래걸린이유
## 1. student 자꾸 studnet 라고씀 => stu로 쓰자
## 2. if문에서 조건걸고 == 를 썼는데 대입할떄도 자꾸 ==로씀. 주의!!!
## lists.count(아무거나)
