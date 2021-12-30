# 1부터 그 수까지 짝수만 합해 출력한다.
# 0~100

a = int(input())
sum = 0

for i in range(1, a+1, 1):
    if(i % 2 == 0):
        sum = sum + i
        
print(sum)
