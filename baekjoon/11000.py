# 강의실 최소 개수
# 

import sys
import heapq

N=int(input())

arr=[]

for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    arr.append([x,y])

arr.sort(key=lambda x: (x[0],x[1]))

heap=[arr[0][1]]

for i in range(1,N):
    if heap[0]<=arr[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,arr[i][1])

print(len(heap))

