
S=input()
collector=[]
sum=0

def collector_sum(collector):
    c_len=len(collector)
    c_sum=0
    for x in collector:
        c_sum=c_sum+int(x)*(10**(c_len-1))
        c_len=c_len-1
    return c_sum

for i in range(len(S)):
    if S[i]==',':
        sum=sum+collector_sum(collector)
        collector=[]
        continue
    
    collector.append(S[i])
    if i==len(S)-1:
        sum=sum+collector_sum(collector)

print(sum)

        

