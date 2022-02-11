https://programmers.co.kr/learn/courses/30/lessons/12926  
<img width="557" alt="image" src="https://user-images.githubusercontent.com/84604563/153523469-dbc56b71-ad2f-4a31-bbe2-d9b3fa3c4c79.png">

```python
# 09:58 ~ 10:14
def solution(s, n):
    al_s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    al_S = ''.join(al_s).upper()
    al_S = list(map(str, al_S))
    
    print(al_s)
    print(al_S)
    
    answer = ''
    
    for i in range(len(s)):
        if s[i].isupper():
            next_i = al_S.index(s[i]) + n
            if next_i >= len(al_S):
                next_i -= 26
            answer += al_S[next_i]
        elif s[i] == ' ':
            answer += ' '
        else:
            next_i = al_s.index(s[i]) + n
            if next_i >= len(al_s):
                next_i -= 26
            answer += al_s[next_i]
    return answer
 ```
 
 ```python
 def solution(s,n):
   s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
 ```
 
 # 배운점
 ## 이런문제는 %연산자 쓰고 ord사용하는게 훨씬 깔끔했을것.
