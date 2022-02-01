![image](https://user-images.githubusercontent.com/84604563/151789579-caaa6f84-9fd7-47fa-abc7-0e18a93b653e.png)


```mysql
-- 코드를 입력하세요
SELECT outs.ANIMAL_ID, outs.NAME
FROM ANIMAL_INS as ins
inner join ANIMAL_OUTS as outs # inner join은 inner 안써줘도 상관x
ON ins.ANIMAL_ID = outs.ANIMAL_ID
ORDER BY outs.DATETIME - ins.DATETIME DESC 
LIMIT 2

# ORDER BY에 연산자를 쓸 수 있다니 정말 신기해!!!
```

배운것 : inner join에서 교집합을 찾고 order by에서 얼마나 오래있었는지(시간차) 구함  
문제에서 datetime 차이로 내림차순으로 정리하라고함. 그래서 order by에서 ```-```연산자 사용(가장 오래 머물러 있었던 순으로 정렬하라)  
