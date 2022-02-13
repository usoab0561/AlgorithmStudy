https://programmers.co.kr/learn/courses/30/lessons/60057

```python
# 09:23 ~ 09:53
# 내가 생각한 sol -> 
# 1. 2개 비교해서 len을 만든다. 이때 stack에 넣어서 숫자랑 길이 만듬 ex) 2a2ba3c
# 2. 3개 비교해서 len을 만든다. ex) [aab] [bac] [cc] 안되면 다음으로
# 3. 4개 비교.. 길이의 절반만큼만 함.
# 
# 실제풀이 : step과 prev를 이용해서 !prev와 지금확인하는거랑!다르면 바로 step으로 넘어감
# prev를 slice이용해서 만들어냄. prev[0:step]... stack이 아니었음!!

def solution(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1
        print(prev)
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            print(j)
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 다시 초기화
                count = 1
            
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        print(compressed)
        # 만들어지는 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer
```
