import sys
import re

input=sys.stdin.readline

N=int(input())

data=[input().strip() for i in range(N)]

# re 라이브러리로 구현
def sort_key(x):
    return sum([int(x) for x in re.findall('[1-9]',x)])

for i in sorted(data,key=lambda x: (len(x), sort_key(x),x)):
    print(i)