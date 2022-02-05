# 고양이와 개는 몇 마리 있을까
문제 설명  
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION,   NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

NAME	TYPE	NULLABLE  
ANIMAL_ID	VARCHAR(N)	FALSE  
ANIMAL_TYPE	VARCHAR(N)	FALSE  
DATETIME	DATETIME	FALSE  
INTAKE_CONDITION	VARCHAR(N)	FALSE  
NAME	VARCHAR(N)	TRUE  
SEX_UPON_INTAKE	VARCHAR(N)	FALSE  
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.  

예시  
예를 들어 ANIMAL_INS 테이블이 다음과 같다면  

ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE  
A373219	Cat	2014-07-29 11:43:00	Normal	Ella	Spayed Female  
A377750	Dog	2017-10-25 17:17:00	Normal	Lucy	Spayed Female  
A354540	Cat	2014-12-11 11:48:00	Normal	Tux	Neutered Male  
고양이는 2마리, 개는 1마리 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.  

ANIMAL_TYPE	count  
Cat	2  
Dog	1  
본 문제는 Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"에서 제공하는 데이터를 사용하였으며 ODbL의 적용을 받습니다.  

```mysql
-- 코드를 입력하세요
SELECT animal_type, count(*)
from animal_ins
group by animal_type
order by animal_type
```

<hr>


![image](https://user-images.githubusercontent.com/84604563/151705896-637c3115-c56f-4aaf-8812-c9d6537920ff.png)

```mysql
select animal_type, count(*) as count
from animal_ins
where animal_type in ('Cat', 'Dog')
group by 1
order by 1
```

group by 1 의미가 위 그림처럼 첫번째 열로 정리를 한다는 말,    
즉 animal_type들을 그룹화해서 animal_type에 맞게 정리해줌  

![image](https://user-images.githubusercontent.com/84604563/151705501-57b9d794-6b36-4602-bea0-7fe70e615b79.png)

```mysql
# -- 코드를 입력하세요
# SELECT animal_type, count(*)
# from animal_ins
# group by animal_type
# order by animal_type
select animal_type, count(*)
from animal_ins
# where animal_type = 'Cat' or animal_type = 'Dog'
where animal_type in ('Cat', 'Dog')
group by animal_type
order by animal_type
```

