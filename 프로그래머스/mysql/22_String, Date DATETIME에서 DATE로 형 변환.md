![image](https://user-images.githubusercontent.com/84604563/151712934-edc70e3a-0c04-4335-980b-634451b7b234.png)


```mysql
-- 코드를 입력하세요
SELECT animal_id, name, date_format(datetime, '%Y-%m-%d')
from animal_ins
```

배운점 1 : date_format(바꿀포맷을원하는컬럼, '%y-%m-%d') 식으로 date_format을 사용하면 원하는 날짜 표현가능  
배운점 2 : %Y 로 하면 20이 앞에 자동으로 붙음
