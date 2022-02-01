https://programmers.co.kr/learn/courses/30/lessons/72410

```python
# 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 규칙에 맞는 아이디를 추천
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
import copy


def solution(new_id):
    # stage_one
    new_id = new_id.lower()
    
    # stage_two
    answer = ''
    for words in new_id:                        # new_id 요소 하나씩 돌면서
        if words.isalnum() or words in '-_.':   # alnum or -_.이라면
            answer += words                     # answer에 하나씩 넣어줌
    
    # stage_three
    while '..' in answer:                   # answer에 '..' 가 연속으로 있으면
        answer = answer.replace('..', '.')  # answer에 '..'을 '.' 으로 바꿔줌
        
    # stage_four
    if answer[0] == '.':                        # str도 str[0] 이런식 접근가능
        answer = answer[1:]                     # 2번째 index부터 끝까지
        
    if len(answer) > 0 and answer[-1] == '.':   # answer[-1] outof range때문에
                                                # len(answer) > 0 해줌.
        answer = answer[:-1]                    # 처음부터 마지막 index제외 넣어줌

    # stage_five
    answer = 'a' if len(answer) == 0 else answer 
        # answer = 'a' if answer == '' else answer
        
    # stage_six
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
        # if len(answer) >= 16:
        #   answer = answer[:15]
        # if answer[-1] == '.':
        #   answer = answer[:-1]
    
    # stage_seven
    while len(answer) <= 2:
        answer = answer + answer[-1]
    
    return answer
```

# 배운것

## join은 ```''.join(list)```로 list가 들어온 것을 str로 바꿔주는것임.   

## str.isalnum()
![image](https://user-images.githubusercontent.com/84604563/151924369-7d894420-bc22-4072-a2dc-c8a5b54c2b71.png)

## for i in str: 해주면 str 요소 하나하나 i로 돈다.
![image](https://user-images.githubusercontent.com/84604563/151924697-a3fbd634-1fa5-4401-a2a7-aa0495866149.png)

## word in '_-.'
```word == '_' or word == '-' or word == '.'```

## while '..' in str:
```python 
while '..' in answer:                 # answer(str)에 '..' 가 연속으로 있으면,
  answer = answer.replace('..', '.')  # answer(str)에 '..'을 '.' 으로 바꿔줌
```  

## str 도 str[-1] , str[0], str[:-1](마지막것 제외) 이런접근가능. 
