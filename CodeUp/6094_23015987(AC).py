a = int(input())
b = input().split()

for i in range(a):
    b[i] = int(b[i])
    
min = b[0]

for i in range(a):
    if min > b[i]:
        min = b[i]

print(min)
