import math
n = input().split(',')
a = int(n[0]+n[1]+n[2])-int(n[0]+n[1])
b = int((10**(len(n[1])+len(n[2])))-(10**len(n[1])))
c = math.gcd(a,b)
print(a//c,"/",b//c)