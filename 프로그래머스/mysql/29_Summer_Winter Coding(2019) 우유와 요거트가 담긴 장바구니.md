![image](https://user-images.githubusercontent.com/84604563/151902184-fa230b65-c22c-4256-947d-3d33d782211e.png)


```mysql
# -- 코드를 입력하세요
# select cart_id
# from cart_products
# where cart_id in(
#     select cart_id
#     from cart_products
#     where name = "Milk"
# ) and name = "Yogurt"
# group by cart_id
# order by id

-- 코드를 입력하세요
select cart_id
from cart_products
where cart_id in(
    select cart_id
    from cart_products
    where name like ('Milk')
) and name like ('Yogurt')
group by cart_id
order by id
```

해결법 : 문제에서 name2개 (milk, yogurt)가 중복된 cart_id를 찾으라고했다. 그래서 subquery사용해야한다고 생각했고, cart_id가 기준이될거라 생각.  
그래서 cart_id가 기준인데, where로 milk먼저 서브쿼리에서 name기준으로 찾고, 밖에서 Yogurt찾아줌.  
배운점 : ```colum like ('content')```나 ```colum = 'content'``` 같으니 .
