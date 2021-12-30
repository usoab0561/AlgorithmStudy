a = int(input())
index = 0
sum = 1
while (sum <= a):
    sum = sum + index
    if sum > a:
      break
    index = index + 1
print(index)
