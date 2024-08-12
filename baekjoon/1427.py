import sys

input=sys.stdin.readline

lst=list(map(int,input().rstrip()))

lst_sorted=sorted(lst,reverse=True)

for i in range(len(lst_sorted)):
    print(lst_sorted[i], end='')