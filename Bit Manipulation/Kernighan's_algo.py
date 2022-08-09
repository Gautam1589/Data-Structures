n=int(input())
cnt=0
while n:
    rsbm=n&-n
    n=n^rsbm
    cnt+=1
print(cnt)