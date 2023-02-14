

n,m=map(int,input().split())

check=min(n,m)
arr=[]

for i in range(n):
    arr.append(list(input()))

answer=0
# 왼쪽 상단부터 시작해서 check*check 사이즈만큼이 될때까지 탐색하고
#answer에 max값 저장

for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i+k)<n) and ((j+k)<m) and (arr[i][j]==arr[i][j+k]==arr[i+k][j]==arr[i+k][j+k]):
                answer=max(answer, (k+1)**2)

print(answer)    
