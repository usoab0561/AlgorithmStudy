![image](https://user-images.githubusercontent.com/84604563/151730081-014d5177-b803-48d9-a32a-5a881490eb86.png)

```mysql
-- 코드를 입력하세요
# 아직 입양을 못간 동물. 그니까 animal_ins에서 animal_outs에 있는거 빼주면됨   
# 가장 오레있었던 동물 3마리 이름, 보호시작일 조회 (order by 보호시작일)
select name, datetime
from animal_ins
where animal_id not in (
    select animal_id from animal_outs)
order by datetime
limit 3
```

방법 : not in subquery사용해서 animal_ins에만 있는 animal_id를 가져왔고 limit을 통해서 3개만 표출해줌.  
배운점 : limits 1,3 이런식으로 사용하면, 1번째 index부터 보여주고 3개만 보여줌. offset으로 더 확실하게 하는 방법도 있음. (근데 굳이 안써도되는듯)  
