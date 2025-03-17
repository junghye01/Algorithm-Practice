# 5원과 2원으로 거스름돈 최소 개수

n=int(input())

cnt=0

while True:
    if n%5==0:# n이 5로 나누어 떨어진다면 5로 나눈 몫을 반환
        cnt+=n//5
        break
    else:
        n-=2 # 5로 나누어 떨어지지 않는다면 2원을 축적
        cnt+=1
    
    if n<0:
        break

if n<0:
    print(-1)
else:
    print(cnt)