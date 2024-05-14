info=[]
for k in range(int(input())):
    info.append(input().split())
q=set(input().split())
r=[]
for e in info:
    if q<=set(e[1:]):
        r.append(e)
if len(r)==0:
    print('Not Found')
else:
    r.sort()
    for e in r:
        print(' '.join(e))