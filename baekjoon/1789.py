# 서로 다른 N개의 자연수 합 : S

# S를 알 때, N의 최댓값

import sys

S=int(sys.stdin.readline().strip())

# 1,2,3,4,5 -> 15
# 1,...,10 -> 55
# 1,....,20 -> 210
lst=list(range(1,100000))
part_sum=0
N=0
for x in lst:
    part_sum=sum(lst[1:x+1])
    if part_sum> S and part_sum-S <x:
        N=x

print(N)