![image](https://user-images.githubusercontent.com/84604563/151793211-4c3ef9e8-83fc-4b77-957f-49c98f82e0da.png)

```mysql
-- 코드를 입력하세요
SELECT id, name, host_id
from places
where host_id in (
    select host_id
    from places
    group by host_id
    having count(host_id) > 1)
order by id
```

배운점 : 어떤 테이블에서 컬럼이 몇번 나왔는지 비교하려면 where colum in ( group by having ) 쓰면 해결됨. where in 기억!! 
