# 입양 시각 구하기(1)
문제 설명  
ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME,   SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.
  
NAME	TYPE	NULLABLE  
ANIMAL_ID	VARCHAR(N)	FALSE  
ANIMAL_TYPE	VARCHAR(N)	FALSE  
DATETIME	DATETIME	FALSE  
NAME	VARCHAR(N)	TRUE  
SEX_UPON_OUTCOME	VARCHAR(N)	FALSE  
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.  

예시  
SQL문을 실행하면 다음과 같이 나와야 합니다.  
  
HOUR	COUNT  
9	1  
10	2  
11	13  
12	10  
13	14 
14	9  
15	7 
16	10  
17	12 
18	16  
19	2  
본 문제는 Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"에서 제공하는 데이터를 사용하였으며 ODbL의 적용을 받습니다.  

```mysql
# -- 코드를 입력하세요
# SELECT hour(datetime), count(hour(datetime))
# from animal_outs
# where hour(datetime) between 9 and 19
# group by 1
# order by 1

-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(hour(datetime)) as COUNT
from animal_outs
group by HOUR
having hour >= 9 and hour <= 19
order by HOUR
```

배운점1 : YEAR, MONTH, DAY, HOUR, MINUTE, SECOND  
배운점2 :having은 group문 밑에 나와야하고 select안에 coulum가져올때 as로 명명하더라도 그 줄에서는 가져올 수 없다.  
*그래서 첫째줄 select ... , count(HOUR) as COUNT에서 count(HOUR)을 인식 못함.*  
배운점3 : between통해서 범위설정 가능  
