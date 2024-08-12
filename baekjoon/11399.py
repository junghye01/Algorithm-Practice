import sys

N=int(sys.stdin.readline().strip())

time_lst=list(map(int,sys.stdin.readline().split()))

# 젤 작은 순으로 나열? 
#1. 최선의 선택
result=0
time_lst.sort()
part_sum=0
for i in range(len(time_lst)):
    part_sum=sum(time_lst[0:i+1])
    result+=part_sum

print(result)