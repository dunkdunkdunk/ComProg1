a,b,c,d = [float(e) for e in input().split()]
maxn,minn=a,a
if b > maxn : maxn = b
if c > maxn : maxn = c
if d > maxn : maxn = d
if b < minn : minn = b
if c < minn : minn = c
if d < minn : minn = d
print(round((a+b+c+d-maxn-minn)/2,2))