import sys

input=sys.stdin.readline

x,y,c=map(float,input().split())

def f(x,y,w):
    h1=(x**2-w**2)**0.5
    h2=(y**2-w**2)**0.5
    c=(h1*h2)/(h1+h2)
    return c

s,e=0,min(x,y)
res=0
threshold=0.000001

while e-s>threshold:
    w=(s+e)/2
    if f(x,y,w)>=c:
        res=w
        s=w
    else:
        e=w

print(round(res,3))