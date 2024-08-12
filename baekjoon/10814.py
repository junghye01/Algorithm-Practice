
N=int(input())

members=[]
for i in range(N):
    age,name=input().split()
    age=int(age)
    members.append((age,i,name))

members.sort(key=lambda x: (x[0],x[1]))

for member in members:
    print(member[0],member[2])