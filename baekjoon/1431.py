import sys

input=sys.stdin.readline

N=int(input())

data=[input().strip() for i in range(N)]

# sorted로 구현
def sort_key(x):
    result=0
    for i in x:
        if i.isdigit():
            result+=int(i)
    return result

for i in sorted(data,key=lambda x: (len(x), sort_key(x),x)):
    print(i)