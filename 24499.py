import sys
from itertools import accumulate

input=sys.stdin.readline


N,K=map(int,input().split())

scores=list(map(int,input().split()))

sumlist=[0]+list(accumulate(scores))
Max=0

for i in range(N):
    if i+K<=N:
        Max=max(Max,sumlist[i+K]-sumlist[i])

    else:
        Max=max(Max,sumlist[N]-sumlist[i]+sumlist[(i+K)%N])

print(Max)
