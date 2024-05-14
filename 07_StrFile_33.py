def read_next(f):
    while True:
        t=f.readline()
        if len(t)==0:
            break
        x=t.strip().split()
        if len(x)==2:
            return x[0],x[1]
    return '',''

_=input().split()
f1,f2=open(_[0]),open(_[1])
d1,d2=read_next(f1);p1,p2=read_next(f2);a=[]
while d1!='' or p1!='':
    if d1!='': a.append([d1[-2:],d1,d2]);d1,d2=read_next(f1)
    if p1!='': a.append([p1[-2:],p1,p2]);p1,p2=read_next(f2)
f1.close();f2.close()
for i,j,k in sorted(a):
    print(j,k)