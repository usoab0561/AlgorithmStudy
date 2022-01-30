![image](https://user-images.githubusercontent.com/84604563/151712606-be45928d-242d-4fe4-8adc-77b561bbf449.png)


```mysql
-- 코드를 입력하세요
SELECT animal_id, 
        name, 
        case
        when sex_upon_intake like '%Neutered%' then 'O'
        when sex_upon_intake like '%Spayed%' then 'O'
        else 'X'
        end as '중성화'
from animal_ins
order by animal_id
```

배운점 1 : 조건문 사용하는법. case when then else end.  
배운점 2 : like 써서 when 이후 넣어 활용.

```
case
when  then
when  then
...
else
end
```
