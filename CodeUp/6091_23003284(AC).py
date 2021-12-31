a,b,c = input().split()
d = 1
a = int(a)
b = int(b)
c = int(c)
 
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)
