import sys
input=sys.stdin.readline
N=int(input())

A=list(map(int,input().split()))

M=int(input())

# 누적 합 계산
prefix_sum=[0]
for num in A:
    prefix_sum.append(prefix_sum[-1]+num)

for m in range(M):
    i,j=map(int,input().split())

    # 구간 합 계산
    result=prefix_sum[j]-prefix_sum[i-1]

    print(result)