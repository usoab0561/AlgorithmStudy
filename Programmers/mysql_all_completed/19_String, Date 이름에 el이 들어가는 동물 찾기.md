![image](https://user-images.githubusercontent.com/84604563/151711060-e7972d3b-4830-4159-8603-a33fd14f0fc7.png)

```mysql
-- 코드를 입력하세요
SELECT animal_id, name
from animal_ins
where animal_type = 'Dog' and name like '%el%'
order by name
```

배운점 1 : colum like '%ab%' 라고 하면, colum에서 ab포함된거 가져옴. __like!!__  
배운점 2 : colum like '%ab' 라고 하면, 마지막에 ab로 된거 가져옴.  
배운점 3 : colum like 'ab%' 라고 하면, ab로 시작하는 것 가져옴.
