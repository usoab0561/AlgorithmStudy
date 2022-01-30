![image](https://user-images.githubusercontent.com/84604563/151711591-4ad35746-ff9e-490b-b843-3f25c0e20640.png)


```mysql
-- 코드를 입력하세요
SELECT  animal_type, ifnull(name, 'No name'), sex_upon_intake
from animal_ins
order by animal_id
```

배운점 1 : select ifnull(name, 'No name') 처럼 가져올때 값이 null이면 바꾸는걸 할 수 있다. ifnull(바꾸고싶은colum, '바꿀것')
