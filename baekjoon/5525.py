N=int(input())
M=int(input())
S=input()

# PN을 생성하고 슬라이싱을 하는 건 시간복잡도가 큼

# PN은 IOI 패턴이 N번 나타나는 문자열, 해당 패턴이 몇 번 나타나는지 보기

i=0
count=0
ans=0

while i<M-1:
    if S[i:i+3]=='IOI':
        count+=1
        if count>=N:
            ans+=1
        i+=2
    else:
        count=0
        i+=1

print(ans)
