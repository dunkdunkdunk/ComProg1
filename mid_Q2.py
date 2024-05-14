import math
a=[float(i) for i in input().split()]
if a[0]>0 and a[1]!=0 and a[2]>1:
    print(round(((2*math.pi)**(-1/2))*(1/a[2])*math.e**((-1/2)*((a[0]-a[1])/a[2])**2),2))
else:
    print("Invalid input")