import sys
from bisect import bisect_left
# bisect_left : 해당 값이 list에 있을 때 index 반환
# 해당 값이 없을 때 오름차순으로 들어갈 시 들어갈 index 반환 
# 꼬여있는 전선 개수 x, 잘라내야 할 최소한의 전선 개수

input = sys.stdin.readline

def lis_length(arr):
    lis=[]
    for num in arr:
        idx=bisect_left(lis,num)
        if idx==len(lis):
            lis.append(num)
        else:
            lis[idx]=num

    return len(lis)

N=int(input())
map_num=list(map(int,input().split()))

result=N-lis_length(map_num)
print(result)