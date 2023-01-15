N,M=map(int,input().split())
lst = list(map(int, input().split()))


prefix_sum=[0]
temp=0
for x in lst:
    temp=temp+x
    prefix_sum.append(temp)

for i in range(M):
    i,j=map(int,input().split())
    sum=prefix_sum[j]-prefix_sum[i-1]
    print(sum)

