![image](https://user-images.githubusercontent.com/84604563/151731703-ca86e912-a417-4464-b8af-8d0b32434394.png)

![image](https://user-images.githubusercontent.com/84604563/151731748-63efa9f1-8305-4164-8df4-52820b992741.png)
![image](https://user-images.githubusercontent.com/84604563/151731730-c2a0d587-7fb5-4200-9460-f09f27556285.png)
![image](https://user-images.githubusercontent.com/84604563/151731738-92cfd2ec-c91c-4c7b-9c82-02aca57a9dd2.png)


```mysql
-- 코드를 입력하세요
# # 아직 입양을 못간 동물. 그니까 animal_ins에서 animal_outs에 있는거 빼주면됨   
# # 가장 오레있었던 동물 3마리 이름, 보호시작일 조회 (order by 보호시작일)
# select name, datetime
# from animal_ins
# where animal_id not in (
#     select animal_id from animal_outs)
# order by datetime
# limit 3

# 밑에는 입양 못간 동물을 left join으로 구현해볼거임
# 입양을 못갔다는것은 ins에서 outs에있는거 제외하고 보여주면됨
select a.name, a.datetime
from animal_ins a left outer join animal_outs b
on a.animal_id = b.animal_id 
where b.animal_id is null # !! 이렇게하면 a와 b 중에서 b가 null인부분, 즉 a에만 있는거 보여줌 !! 
                          # a에서 모든것들을 가져오는데, a기준으로 가져와서 a에 없는 내용은 b테이블에서는 null로 표현해서라도 가져옴.  
order by datetime
limit 3
```

배운점 
```mysql
select a.name, a.datetime
from animal_ins a left outer join animal_outs b
on a.animal_id = b.animal_id 
```
이거나    
```mysql  
select a.name, a.datetime
from animal_ins a 
```
이거나 같다. 왜? on은 fk 조인을 해준다고 하는거라서 어차피 여기에서는 left join이랑 같은역할로 a 부분만 보여줌.  
