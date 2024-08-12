import sys
T=int(sys.stdin.readline())

def factorial(n): # mCn = m! / (m-n)!n!
    result=1
    for i in range(1,n+1):
        result=result*i
    return result


for _ in range(T):
    n,m=map(int,sys.stdin.readline().split())
    bridge=factorial(m)// (factorial(m-n)*factorial(n))
    print(bridge)

