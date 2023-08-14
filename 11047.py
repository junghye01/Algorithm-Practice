import sys

input=sys.stdin.readline


N,K=map(int,input().split())

lst=[]
for i in range(N):
    lst.append(int(input()))

count=0

for c in reversed(lst):
    count+=K//c
    K=K%c


print(count)
    

