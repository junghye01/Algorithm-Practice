import sys
n=int(sys.stdin.readline())
num=[0]*10001

# 입력값의 개수가 극한으로 주어질 수 있음
# 메모리를 효율적으로 관리하기 위해 미리 10001 크기의 리스트 형성
for _ in range(n):
    num[int(sys.stdin.readline())]+=1

for i in range(10001):
    if num[i]!=0:
        for j in range(num[i]): # 1 1 이런식으로 같은 숫자가 2번 있을수도
            print(i)

