n = int(input())
inputs = input().split()

for i in range(n): #0~n-1까지
    inputs[i] = int(inputs[i])
    
list = [] # 리스트만들기

for i in range(24): #0~23까지
    list.append(0)  #0넣어주기

for i in range(n):
    list[inputs[i]] += 1
    
for i in range(1,24):
    print(list[i], end=' ')

