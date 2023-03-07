# 2-2 -> 1
# 2-3 -> 3
# 4-5 -> 5 
# MCN 을 구하면 됨
# nCr=n! / (n-r)! r!
# 주의 : 시간 제한 0.5s라 sys라이브러리 사용
import sys
T=int(sys.stdin.readline().strip())


def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

for i in range(T):
    N,M=map(int,sys.stdin.readline().split())
    final_result=factorial(M)/(factorial(M-N)*factorial(N))
    print(int(final_result))
    
