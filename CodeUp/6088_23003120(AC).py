# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램을 만들어보자.
# 1 4 7 10 13 
a,d,n = input().split()
a = int(a)
d = int(d)
n = int(n)

for i in range(1,n):
    a += d
print(a)
