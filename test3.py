import math

data=zip([1,2,3,4,5],[4,5,14,12,20])
mean_x=sum([1,2,3,4,5])/5
mean_y=sum([4,5,14,12,20])/5
mol=0
xresult=0
yresult=0

for x,y in data:
    mol=mol+(x-mean_x)*(y-mean_y)
    xresult=xresult+pow((x-mean_x),2)
    yresult=yresult+pow((y-mean_y),2)


result=mol/math.sqrt(xresult*yresult)

print(result)