﻿r,g,b = input().split()
cnt = 0
r = int(r)
g = int(g)
b = int(b)

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i,j,k)
            cnt = cnt+1

print(cnt)
