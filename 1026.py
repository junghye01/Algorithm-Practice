# B는 고정, A의 모든 경우의 수를 구해서 최솟값 찾기
# 어떻게 하면 최솟값 -> 가장 큰수 * 작은수 의 합
import sys
n=int(sys.stdin.readline().strip())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

final_result=0
# 가장 큰 수와 가장 작은수를 곱하고 제외시키는 식으로
#for i in range(len(A)):
 #   max1=max(A)
  #  min1=min(B)
   # max2=max(B)
    #min2=min(A)
    #result1=max1*min1
    #result2=max2*min2
    #result=min(result1,result2)
    #if result==result1:
     #   A.remove(max1)
      #  B.remove(min1)
    #else:
     #   A.remove(min2)
      #  B.remove(max2)
    #final_result+=result

# short ver : A를 오름차순으로, B를 내림차순으로 하고 곱하기
# 주의 : list.sort() : 리스트 자체 정렬 (default: 오름차순)
# sorted_a=sorted(a) # 새로운 정렬된 리스트 반환 (default:오름차순?)
sorted_a=sorted(A)
sorted_b=sorted(B,reverse=True)

for i in range(n):
    final_result+=sorted_a[i]*sorted_b[i]
print(final_result)
    