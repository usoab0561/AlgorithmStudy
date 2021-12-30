end = ord(input())
start = ord('a')
while(start <= end):
    if(start != end):
        print(chr(start),end=' ')
    elif(start == end):
        print(chr(start), end='')
    start = start+1

