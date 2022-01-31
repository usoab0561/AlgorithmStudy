![image](https://user-images.githubusercontent.com/84604563/151791842-02b40084-219d-4416-aa7a-d75b7271e32e.png)

```mysql
-- 코드를 입력하세요
select ins.animal_id, ins.name
from animal_ins as ins
join animal_outs as outs
on ins.animal_id = outs.animal_id
where outs.datetime < ins.datetime
order by ins.datetime # 문제에 보면 '보호 시작일이 빠른 순으로 조회' 라고함. 이말은 즉슨 보호 들어온 (ins)가 빠른순 (오름차순)
```

배운점 1 : order by 에서 비교연산자 쓰는거는 서로의 차를 구할때 쓰는거고, 보통 where절안에서 그 차이를 구함.  
