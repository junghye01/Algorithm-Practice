# A->B 로 만드는 최소 연산 횟수
# B->A (top-down 방식)
# 끝에 1이 있다면 1을 빼기 
# 아니면 2로 나누기


a,b=map(int,input().split())

result=1

while(b!=a):
    result+=1
    temp=b # 연산 전
    if b%10==1:
        b//=10
    elif b%2==0:
        b//=2

    if temp==b:
        print(-1)
        break

else:
    print(result)

        
