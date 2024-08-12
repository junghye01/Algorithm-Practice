# 회의의 최대 개수
# i 번째 회의 끝나는 시간 <= j번째 회의 시작 시간
import sys
N=int(input())

arr=[]

for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    arr.append([x,y])

answer : int=0
endPoint : int=0

arr.sort(key=lambda x : (x[1],x[0]))
for newstart,newend in arr:
    if endPoint<=newstart:
        answer+=1
        endPoint=newend

print(answer)