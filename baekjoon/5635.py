import sys
input=sys.stdin.readline

N=int(input())

info=[]
for i in range(N):
    name,day,month,year=input().split()
    info.append([name,int(day),int(month),int(year)])

info.sort(key=lambda x: (x[3],x[2],x[1]))

print(info[-1][0])
print(info[0][0])