![image](https://user-images.githubusercontent.com/84604563/151905565-8f2c1857-751f-4ca1-8ae8-c13fc0d78117.png)

```mysql
-- 코드를 입력하세요
# 중성화x : Intact
# 중성화o : Spayed or Neutered
# ins일때는 Intact지만 outs일때는 Spayed or Neutered

select ins.animal_id, ins.animal_type, ins.name
#ins.SEX_UPON_INTAKE , outs.SEX_UPON_OUTCOME
from animal_ins as ins
inner join animal_outs as outs
on ins.animal_id = outs.animal_id
where ins.SEX_UPON_INTAKE like ('%Intact%')
and outs.SEX_UPON_OUTCOME  in (
    select SEX_UPON_OUTCOME
    from animal_outs
    where SEX_UPON_OUTCOME like ('%Neutered%') or SEX_UPON_OUTCOME like ('%Spayed%')
) 

# select ins.animal_id, ins.animal_type, ins.name
# from animal_ins as ins
# inner join animal_outs as outs
# on ins.animal_id = outs.animal_id
# where 
#     ins.SEX_UPON_INTAKE like ('%Intact%') and
#     (outs.SEX_UPON_OUTCOME like ('%Neutered%') or 
#     outs.SEX_UPON_OUTCOME like ('%Spayed%'))
```

ins일때는 Intact지만 outs일때는 Spayed or Neutered인것을 구하는 문제. 
1. inner join으로 공통된 id를 찾고  
2. 서브쿼리 이용해서 Spayed or Neutered인 것을 sex_upon_outcome기준으로 찾아준다. ```() 괄호```통해서 아래와같이 편하게 연산자 이용할 수도 있다.
