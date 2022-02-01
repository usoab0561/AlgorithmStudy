![image](https://user-images.githubusercontent.com/84604563/151903203-072e42de-cf1e-499b-af83-26132dcf329d.png)

![image](https://user-images.githubusercontent.com/84604563/151903220-274a248d-71bf-4569-ad0e-cba30470fe6e.png)


```mysql
# SET @HOUR = -1;
# SELECT (@HOUR := @HOUR +1) AS HOUR
# FROM ANIMAL_OUTS
# WHERE @HOUR < 23;
# 위 코드는 일단 0 ~ 23을 HOUR로 표기해줌. SET @SOMETHING에서 꼭 마지막에 ; 써줘야함.

SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME)) 
    FROM ANIMAL_OUTS 
    WHERE HOUR(DATETIME)=@HOUR) 
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
```
![image](https://user-images.githubusercontent.com/84604563/151709340-66957190-4501-4076-94fa-4c035130f2e4.png)

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=pyj721aa&logNo=221466664622
