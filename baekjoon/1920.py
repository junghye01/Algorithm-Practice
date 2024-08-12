import time

start=time.time()
N=int(input())

A=set(map(int,input().split()))

M=int(input())

B=list(map(int,input().split()))

for x in B:
    if x in A:
        print('1')
    else:
        print('0')

print('걸린 시간',time.time()-start)