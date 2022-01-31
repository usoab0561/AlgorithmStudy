![image](https://user-images.githubusercontent.com/84604563/151728845-fc1f3680-5e32-4765-952d-a54c9fd410d3.png)

# 테이블 animal_ins(입양들어온), animal_outs(입양나간), fk 는 animal_id  

```mysql
# -- 코드를 입력하세요
# out은 있는데 in이 없는 id, name을 보여줘라.
# right join으로 out만 있는것을 보여주면 될듯?
# 그렇게 하면 됐다.
# SELECT b.animal_id, b.name
# from animal_ins a right outer join animal_outs b # outer 굳이 안해줘도 됨.
# on a.animal_id = b.animal_id
# where a.animal_id is null

# 밑에 코드는 a(animal_outs)기준 left조인 해서 A-B 차집합 보여줌.
# -- 코드를 입력하세요
# SELECT A.ANIMAL_ID, A.NAME
# FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B
# ON A.ANIMAL_ID = B.ANIMAL_ID
# WHERE B.ANIMAL_ID IS NULL

# 서브쿼리 not in 사용해서, animal_outs에는 있고 animal_ins에 없는는거 제외해서 보여줌.
select animal_id, name
from animal_outs
where animal_id not in (
        select animal_id from animal_ins)
```

방법 1 : right join으로 animal_outs에 있는 것만 보여줌. on을 사용해서 fk정리해주고 where 통해 차집합 제대로 표현해줌.  
방법 2 : left join으로 anilmal_outs에 있는 것만 보여줌. 똑같음.  
방법 3 : not in 서브쿼리를 where 부분에서 사용해서 animal_id를 animal_outs에서 가져오는데, animal_ins에 없는거 지워줌
