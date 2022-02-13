https://luv-n-interest.tistory.com/736
<img width="978" alt="image" src="https://user-images.githubusercontent.com/84604563/153734773-1df14e73-cd83-4d08-b175-cb1a4f4e001e.png">

```python
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
```    
1. 일단 점 지나는거는 최대공약수개수만큼임
2. 최대공약수1일때, 사각형 곂치는게 w+h-1임 
3. 그러니까 최대공약수개수 * 곂치는거. 그런데 최대공약수 1일때 만드려면 최대공약수만큼 나눠줘야함.. 이해안가면 블로그 천천히보면 이해감

