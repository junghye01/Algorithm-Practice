import math
data=[7.28,8.54,15.28,5.51,3.17,6.34,3.8,4.59,5.12,9.98,7.04,10,11.96,5.48,2.3,5.85,9.39,8.73,7.66]

len_data=len(data)
data.sort()
print('정렬값',data)
print('10',data[9])
print('15',data[14])
sum=0
mean=7.26
for x in data:
    sum=sum+pow((x-mean),2)

result=math.sqrt(sum/18)

print(result)
