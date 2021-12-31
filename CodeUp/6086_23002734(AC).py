a = int(input())
sum = 0
cnt = 0
while True:
    cnt += 1
    sum += cnt 
    if sum >= a:
        break
    
print(sum)
