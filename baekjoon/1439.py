import sys
S=list(sys.stdin.readline().strip())

# 연속된 숫자를 하나로 잡아서 뒤집어서 같은 수로
# 최소 뒤집는 수
"""
입력받은 string 수 -> 변화 횟수 -> 뒤집어야할 횟수
0 -> 0 -> 0
01 -> 1 -> 1
010 -> 2 -> 1
0101 -> 3 -> 2
01010 -> 4 -> 2
010101-> 5 -> 3
0101010 -> 6 -> 3

뒤집어야 할 횟수 : (count+1)//2 하고 몫(//)만
"""
count=0
pre=S[0]
for x in S :
    if pre!=x:
        count=count+1
    pre=x

print((count+1)//2)


